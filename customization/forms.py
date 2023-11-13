from django import forms
from accounts.models import UserAccount

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = [
            'profile_image',
            'profile_cover',
            'profile_song',
            'profile_background',
            'hide_email',
            'bio',
            'location',
            'color',
            'backgroundColor',
            'font_preference',
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].required = False
        self.fields['profile_cover'].required = False
        self.fields['profile_song'].required = False
        self.fields['profile_background'].required = False
        self.fields['hide_email'].required = False
        self.fields['bio'].required = False
        self.fields['location'].required = False
        self.fields['color'].required = False
        self.fields['backgroundColor'].required = False
        self.fields['font_preference'].required = False