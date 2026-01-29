from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("hello world")

def AboutUs(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")


def home(request):
    return render(request,"home.html")

def reacp(request):
    return render(request,"reacp.html")


def recipe(request):
    ingredient = ["meggie","tomato"]
    data = {"name":"meggie","time":20,"ingredient":ingredient}
    return render(request,"recipe.html",data)

def team(request):
    playerlist = ["ms dhoni","urvil patel","ruturaj gaikwad","sanju samson","dewald brevis","pathirana","ravindra jadeja"]
    data = {"team name": "csk","trophy":5,"captain":"ms dhoni","players": playerlist,}
    return render(request,"team.html",data)