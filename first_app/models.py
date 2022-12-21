from django.db import models

class basic_field(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    is_basic_class = models.BooleanField()
    email = models.EmailField(max_length=200)
    address = models.TextField(max_length=255)
class ex_field(models.Model):
    upload = models.FileField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    Date_purchase = models.DateTimeField()
    product = models.ImageField()

class duble_ex_field(models.Model):
    timeof_dispatch = models.TimeField()
    url = models.URLField(max_length=200)
