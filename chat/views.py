from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


@login_required
def index(request):
  return render(request, 'chat/index.html')

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
