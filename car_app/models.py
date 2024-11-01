from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_type = models.CharField(max_length=20)
    doors = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return self.car_name

class CarModel(models.Model):
    model_name = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=10)
    colour = models.CharField(max_length=10)
    price = models.IntegerField()
    quantity = models.IntegerField()
    year = models.DateField(auto_now_add=True,blank=True,null=True)
    description = models.TextField()
    brand = models.ForeignKey(Car,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_app/uploads',blank=True,null=True)
    def __str__(self):
        return f'model : {self.model_name}'