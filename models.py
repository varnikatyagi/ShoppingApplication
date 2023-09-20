from django.db import models

# Create your models here.
# in this module we're going to create a new class called product. so now we need to inherit 
# the class from the model class in django so from line 1 from django.db package  we are importing
# the models module .In this module  we have a class called model and this class defines all the 
# common characterstics and behavior for models in a django application 

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)


class Offer(models.Model):
    couponcode=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()
