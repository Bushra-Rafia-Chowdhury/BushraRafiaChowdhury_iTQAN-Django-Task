from django.db import models

# Create your models here.
class vegetables(models.Model):
    id = models.CharField(max_length=20,primary_key = True)
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.id

class fruits(models.Model):
    id = models.CharField(max_length=20,primary_key = True)
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.id

class beverages(models.Model):
    id = models.CharField(max_length=20,primary_key = True)
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.id

class babies(models.Model):
    id = models.CharField(max_length=20,primary_key = True)
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.id

class bread_bakery(models.Model):
    id = models.CharField(max_length=20,primary_key = True)
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    def __str__(self):
        return self.id