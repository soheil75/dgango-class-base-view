from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class UserLogin(auth_views.LoginView):
    template_name = 'accounts/login.html'
    extra_context = {'name': 'soheil'}


class UserPassReset(auth_views.PasswordResetView):
    email_template_name = 'accounts/password_reset_email.html'
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'accounts/reset_done.html'

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
