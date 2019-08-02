from django.shortcuts import render
from .models import Checkin
from .forms import CheckinForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'vehicle_movement/index.html')

def CheckinView(request):
    if request.method == "POST":
        checkin_form = CheckinForm(data = request.POST)
        if checkin_form.is_valid():
            checkin_form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            HttpResponse("Error")
    else:
        checkin_form = CheckinForm()
    return render(request,'vehicle_movement/checkin.html',{'checkin_form':checkin_form})

def listView(request):
    vehicle_list_load = list(Checkin.objects.all().filter(Type ='Loading'))
    vehicle_list_unload = list(Checkin.objects.all().filter(Type ='Unloading'))
    return render(request,'vehicle_movement/listView.html',{'vehicle_list_load':vehicle_list_load,
    'vehicle_list_unload':vehicle_list_unload})
