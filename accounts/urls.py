from django.urls import path
from .views import SignupView, logout_view, send_mail

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout_view, name='log_out'),
    # path('password_reset/done/', send_mail, name='password_reset'),
]

