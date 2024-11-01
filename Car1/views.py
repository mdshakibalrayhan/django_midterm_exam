from django.shortcuts import render
from car_app.models import CarModel,Car
def home(request,category_slug=None):
    data = CarModel.objects.all()
    if category_slug is not None:
        car_brand = Car.objects.get(id=category_slug)
        data = CarModel.objects.filter(brand=car_brand)
    car_brand = Car.objects.all()
    return render(request,'home.html',{'data':data,'car_brand':car_brand})
