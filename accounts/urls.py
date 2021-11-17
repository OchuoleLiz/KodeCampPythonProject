from django.urls import path
from .views import SignUpView, AccountUpdateView, AccountDeleteView, AccountDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/profile/', AccountDetailView.as_view(), name='profile'),
    path('<int:pk>/update/', AccountUpdateView.as_view(), name='account_update'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),    
]