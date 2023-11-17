from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from accounts.models import UserAccount

UserModel = get_user_model()
class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        users = UserModel._default_manager.filter(
            Q(**{f"{UserModel.USERNAME_FIELD}__iexact": username}) |
            Q(**{"email__iexact": username})
        )

        for user in users:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None
class UserDoesNotExistError(Exception):
    pass

class UserDoesNotExistOrInactiveError(Exception):
    pass
class AuthenticationEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            pass
        return None


    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            raise UserDoesNotExistError("User does not exist")