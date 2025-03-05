from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
def home (request):
    return render (request , "index.html")

def signin (request):
    print("you did a"+request.method)
    if request.method == "POST":
        print( request.POST)
        typedusername = request.POST.get("username") 
        print("the typed username is :" +typedusername)
        typedpassword= request.POST.get("password")
        print("the typed password is :"+typedpassword)
        answer=authenticate( username = typedusername , password = typedpassword)
        if answer==None:
            return HttpResponse("you aren't registered with us")
        else:
            login(request , answer)
            return redirect("home")
        
    return render (request , "signin.html")

def signup(request):
    print("you did a"+request.method)
    if request.method == "POST":
        print( request.POST)
        typedEmail = request.POST.get("Email") 
        print("the typed email is :" +typedEmail)

        typedFirstName= request.POST.get("FirstName")
        print("the typed password is :"+typedFirstName)

        typedLastName = request.POST.get("LastName") 
        print("the typed LastName is :" +typedLastName)

        typedUsername = request.POST.get("Username") 
        print("the typed Username is :" +typedUsername)
    
        typedPassword= request.POST.get("Password")
        print("the typed Password is :"+typedPassword)
        new_password= make_password(typedPassword)
        new_user=User(first_name =typedFirstName , last_name=typedLastName ,email=typedEmail , username=typedUsername , password=new_password)
        new_user.save()
        return redirect("signin")
    return render (request , "signup.html")
 
def Signout(request):
    logout(request)
    return redirect("signin")