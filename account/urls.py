from account.views import RegisterView
from django.urls import path

from .views import ActivateAccountView, RegisterView, activate_account_send_view, activate_account_done_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/activate/', activate_account_send_view, name='activate_send'),
    path('register/activate/done/', activate_account_done_view, name='activate_done'),
    path('register/activate/<slug:uidb64>/<slug:token>/', ActivateAccountView.as_view(), name='activate_account'),
]
