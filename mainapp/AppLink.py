from .views import homepage
from.views import aboutuspage
from.views import Loginpage
from.views import movie_page
from.views import fetch_all_Players_page 
from.views import  fetch_all_movie_page
from.views import fetch_one_players_page
from.views import update_one_movie_page
from.views import fetch_one_movie_page
from django.urls import path
from.views import delete_one_Player
urlpatterns = [
    path ("homepage/", homepage, name="homepage"), 
    path ("aboutuspage/", aboutuspage, name="aboutaupage"), 
    path ("Loginpage/" ,Loginpage,name="Loginpage"),
    path("movie_page/", movie_page,name="movie_page"),
    path("allplayerspage" , fetch_all_Players_page, name ="allplayerspage"),
    path("all_movie_page" ,fetch_all_movie_page, name="all_movie_page"),
    path("oneplayerpage/<int:pk>", fetch_one_players_page, name="oneplayerpage"),
    path("one_movie_page/<int:pk>", fetch_one_movie_page, name="one_movie_page"),
    path("update_one_movie_page/<int:pk>", update_one_movie_page, name="update_one_movie_page"),
    path("delete_one_Player/<int:pk>", delete_one_Player , name="delete_one_Player"),
]
