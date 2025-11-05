from allauth.account.forms import SignupForm
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail


class SignUpUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['email'].label = 'Адрес электронной почты'
        self.fields['password1'].label = 'Введите пароль'
        self.fields['password2'].label = 'Подтвердите пароль'

        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def save(self, request):
        user = super().save(request)
        basic_group = Group.objects.get(name='author')
        basic_group.user_set.add(user)
        html_content = (
            f'<p>Привет, {user.username}!</p>'
            '<p>Вы успешно прошли регистрацию на '
            f'<a href="{settings.SITE_URL}">Новостном портале</a>!'
        )
        send_mail(
            subject='Регистрация',
            message='Вы успешно прошли регистрацию на портале!',
            html_message=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user
