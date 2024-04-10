from django.http import HttpResponse
from django.shortcuts import render

from PekainExpress.models import MesTrains

# Create your views here.
def index(request) : 
    listeTousTrain = MesTrains.objects.all()
    return render(request, "train/index.html",{
        "listeTrains" : listeTousTrain[0]
    })


def show(request, trainId) :
    premierTrain = MesTrains.objects.all()[0]
    return render(request, "train/show.html", {
        "nom" : premierTrain.name,
        "terminus" : premierTrain.terminus,
        "hour" : premierTrain.hour,
        "nextId" : int(trainId) + 1
    })



def random(request, train) :
    return render(request, "PekainExpress/random.html", {})

MesTrains