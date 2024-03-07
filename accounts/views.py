from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect

from config import settings
from .forms import CustomUserCreateForm


class SignupView(CreateView):
    form_class = CustomUserCreateForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')


def logout_view(request):
    logout(request)
    return redirect('home')


# def send(request):
#     send_mail(
#         'Email Subject here',
#         'Email content',
#         from_email=False,
#         recipient_list=['emailto@gmail.com'],
#         settings.EMAIL_HOST_USER,
#
#         html_message='password_reset_email.html',
#         fail_silently=False)
