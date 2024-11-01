from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import CarOwner
from car_app.models import CarModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request,id):
    car_owner = User.objects.get(pk=id)
    car = CarOwner.objects.filter(owner=id)
    print(car)
    all_cars = []
    for c in car:
        CAR =CarModel.objects.get(model_name = c.owned_car)
        print(all_cars.count(CAR))

        all_cars.append(CAR)
    
    print(all_cars,len(all_cars),"  ",'cars filtered from carModel')
    return render(request,'profile.html',{'data':car_owner,'car':all_cars})
