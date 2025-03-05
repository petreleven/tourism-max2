from django.urls import path
from.views import home
from.views import signin
from.views import signup
from.views import Signout
urlpatterns = [
path("home" , home,name="home"),
path("signin" , signin ,name="signin"),
path("signup" , signup , name="signup"),
path("Signout" , Signout , name="Signout"),
]