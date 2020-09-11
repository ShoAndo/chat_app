from django.urls import path
from . import views

urlpatterns = [
  path('', views.index , name="index"),
  path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
]