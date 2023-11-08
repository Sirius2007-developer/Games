from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='product/img')

    def __str__(self):
        return self.name
class Control(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name

class Remote(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='remot/img')

    def __str__(self):
        return self.name

class Quote(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    text = models.TextField()

    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='about/img')

    def __str__(self):
        return self.name

class Thing(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='remot/img')

    def __str__(self):
        return self.name



