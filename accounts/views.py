from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from accounts.models import Account
from accounts.forms import AccountUserCreationForm

class SignUpView(CreateView):
    model = Account
    form_class = AccountUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class AccountDetailView(UpdateView):
    model = Account
    template_name = 'registration/user_proile.html'
    

class AccountUpdateView(UpdateView):
    model = Account
    fields = ('first_name', 'last_name',)
    template_name = 'registration/account_update.html'
    success_url = reverse_lazy('login')

class AccountDeleteView(DeleteView):
    model = Account
    fields = '__all__'
    template_name = 'registration/account_delete.html'
    success_url = reverse_lazy('signup')