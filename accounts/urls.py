from django.urls import path
from .views import PasswordReset, SignUpView, AccountUpdateView, AccountDeleteView, AccountDetailView, LoginRedirect, PasswordChange
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login', LoginRedirect.as_view(), name='profile'),
    path('<int:pk>/profile/', AccountDetailView.as_view(), name='profile'),
    path('<int:pk>/update/', AccountUpdateView.as_view(), name='account_update'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),  
    path('password_change/done', PasswordChange.as_view(), name='password_change_done'), 
    path('password_change/', PasswordReset.as_view(), name='password_reset'),           
]          