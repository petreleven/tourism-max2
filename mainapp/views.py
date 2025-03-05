from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Players
from.models import Movie
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
    return HttpResponse("hello python")

def aboutuspage( request ):
    return HttpResponse ("<h1> My Email is  thegoat@gmail.com </h1>")

def Loginpage ( request:HttpRequest):
    #return HttpResponse("<input> <input>")
    print("you did a"+request.method)
    if request.method == "POST":
        print( request.POST)
        typedname = request.POST.get("username") 
        print("the typed name is :" +typedname)
        typedpassword = request.POST.get("password")
        print("the typedpassword password is :"+typedpassword)
        new_player = Players(username=typedname , password=typedpassword)
        new_player.save() #saving player
    return render(request , "login.html")

def movie_page(request:HttpRequest):
    print("you did a"+request.method)
    if request.method == "POST":
        print( request.POST)
        typedmovie = request.POST.get("moviename") 
        print("the typed moviename is :" +typedmovie)
        typeddescription= request.POST.get("description")
        print("the typeddescription descripiton is :"+typeddescription)
        new_Movie = Movie (name=typedmovie , descripiton=typeddescription , rate = 0) 
        new_Movie.save()
    return render(request , "createmovie.html")

def fetch_all_Players_page (request):
    all_Players = Players.objects.all()
    return render (request , "all_player.html" , {"all_Players":all_Players})
def fetch_all_movie_page (request):
    all_Movie = Movie.objects.all()
    return render (request ,"movies_page.html"  , {"all_Movie":all_Movie} )

def fetch_one_players_page(request , pk): #which play or person 1,7, 18 ,2
    single_player = Players.objects.get(pk = pk)
    return render (request, "one_player.html" , {"single_player":single_player})

def fetch_one_movie_page(request , pk):
    single_Movie = Movie.objects.get(pk=pk)
    return render (request , "one_movie_page.html ", {"single_Movie":single_Movie})
def update_one_movie_page(request , pk ):
    single_movie = Movie.objects.get(pk = pk)
    return render(request, "update_one_movie.html",{"single_movie": single_movie})

def delete_one_Player(request , pk):
	single_Players = Players.objects.get(pk = pk)
	single_Players.delete()
	return redirect ("homepage")