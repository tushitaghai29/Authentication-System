from django.urls import path
from api.views import login, viewdetails, signup, update

urlpatterns = [
    path("user/signin/", login.Login.as_view()),
    path("user/display/", viewdetails.Display.as_view()),
    path("user/signup/", signup.Signup.as_view()),
    path("user/update/", update.Update.as_view()),
]
