# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from models import User
import re


class SignUpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder': u'이메일'}),
        label=''
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': u'사용자 이름'}),
        label=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': u'비밀번호'}),
        label=''
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].error_messages = {
            'required': u"이메일을 입력해주세요.",
            'invalid': u"올바르지 않은 이메일입니다."
        }
        self.fields['username'].error_messages = {'required': u"사용자 이름을 입력해주세요."}
        self.fields['password'].error_messages = {'required': u"비밀번호를 입력해주세요."}

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@hanyang.ac.kr'):
            raise forms.ValidationError(self.fields['email'].error_messages['invalid'])
        if User.objects.filter(email=email).count():
            raise forms.ValidationError(u"이미 등록된 이메일입니다.")

        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise forms.ValidationError(u"사용자 이름의 길이가 너무 짧습니다.")
        if User.objects.filter(username=username).count():
            raise forms.ValidationError(u"이미 존재하는 사용자 이름입니다.")
        if not re.match(r"^[A-Za-z0-9]+$", username):
            raise forms.ValidationError(u"사용자 이름에는 알파벳 대소문자, 숫자만 사용 가능합니다.")

        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 5:
            raise forms.ValidationError(u"비밀번호의 길이가 너무 짧습니다.")
        return password

    def sign_up(self, request):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.create_user(email, username, password)

        return user


class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder': u'이메일'}),
        label=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': u'비밀번호'}),
        label=''
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['email'].error_messages = {'required': u"메일을 입력해주세요."}
        self.fields['password'].error_messages = {'required': u"비밀번호를 입력해주세요."}

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("이메일 혹은 비밀번호를 확인해주세요.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
