from django.db import models
from car_app.models import CarModel
from django.contrib.auth.models import User
# Create your models here.
class CarOwner(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    owned_car = models.CharField(max_length=30,blank=True,null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)