# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
from forms import LoginForm, SignUpForm


def anonymous_required(view_function, redirect_to=None):
    return AnonymousRequired(view_function, redirect_to)


class AnonymousRequired(object):

    def __init__(self, view_function, redirect_to):
        if redirect_to is None:
            from django.conf import settings
            redirect_to = settings.LOGIN_REDIRECT_URL
        self.view_function = view_function
        self.redirect_to = redirect_to

    def __call__(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated():
            return redirect(self.redirect_to)
        return self.view_function(request, *args, **kwargs)


@anonymous_required
def sign_up(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.sign_up(request)
        messages.success(request, '아이디가 생성됐습니다.')
        return redirect('/login')

    return render(request, 'users/sign_up.html', {
        'form': form,
    })


@anonymous_required
def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.login(request)
        if user:
            auth_login(request, user)
            return redirect('/')

    return render(request, 'users/login.html', {
        'form': form,
    })


def logout(request):
    if request.user is not None and request.user.is_authenticated():
        auth_logout(request)
    return redirect('/')
