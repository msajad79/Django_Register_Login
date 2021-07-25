from django.urls import path
from django.contrib.auth.decorators import login_required

from account.views import RegisterView

from .views import (ActivateAccountView, RegisterView, LoginView, ProfileView,
                    activate_account_done_view, activate_account_send_view)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/activate/', activate_account_send_view, name='activate_send'),
    path('register/activate/done/', activate_account_done_view, name='activate_done'),
    path('register/activate/<slug:uidb64>/<slug:token>/', ActivateAccountView.as_view(), name='activate_account'),

    path('login/', LoginView.as_view(), name='login'),

    path('profile/', login_required(ProfileView.as_view()), name='profile')
]
