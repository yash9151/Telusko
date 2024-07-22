from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The City hat Never Sleeps"
    dest1.img = "destination_1.jpg"
    dest1.price = 750

    dest2 = Destination()
    dest2.name = "Pune"
    dest2.desc = "The City of Education"
    dest2.img = "destination_2.jpg"
    dest2.price = 1000

    dest3 = Destination()
    dest3.name = "Delhi"
    dest3.desc = "The City with Pollution"
    dest3.img = "destination_3.jpg"
    dest3.price = 800

    dests =[dest1, dest2, dest3]

    return render(request, "index.html",{"dests":dests})