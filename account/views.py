from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.contrib.auth.models import User

from .forms import RegisterForm
from .tokens import account_activation_token


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register/register.html',context={'form':form})

    def post(self, request):
        form  = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.is_active = False
            user.save()
            curent_site = get_current_site(request)
            subject = 'Active your account'
            message = render_to_string(
                'register/message_send_mail.html',
                {
                    'user': user,
                    'domain': curent_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user)
                }
            )
            user.email_user(subject, message)
            return redirect('activate_send')
        else:
            form = RegisterForm()
        return render(request, 'register/register.html',context={'form':form})


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if not user is None and account_activation_token.check_token(user,token):
            user.is_active = True
            user.save()
            return render(request, 'register/confirm_mail_done.html')
        return render(request, 'register/confirm_mail_invalid.html')


def activate_account_send_view(request):
    return render(request, 'register/confirm_mail.html')


def activate_account_done_view(request):
    return render(request, 'register/confirm_mail_done.html')
