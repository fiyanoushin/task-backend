
from django.urls import path
from .views import RegisterView, LoginView, ProjectList



urlpatterns = [
   path("register/", RegisterView.as_view()),
   path("login/", LoginView.as_view()),
   path("projects/", ProjectList.as_view()),
]
