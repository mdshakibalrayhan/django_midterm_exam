from django.db import models
from car_app.models import CarModel
# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)
    comment_for = models.ForeignKey(CarModel,on_delete=models.CASCADE)
