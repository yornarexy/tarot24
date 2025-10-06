from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpUserForm

class SignupView(CreateView):
    model = User
    form_class = SignUpUserForm
    template_name = 'sign_up/signup.html'
    success_url = reverse_lazy('login')


