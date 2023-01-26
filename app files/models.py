from django.db import models


class regmodel(models.Model):
    fname=models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    email=models.EmailField()
    phno=models.IntegerField()
    passw=models.CharField(max_length=20)
    cpassw=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)

# Create your models here.
class storemodel(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class bookmodel(models.Model):
    bname=models.CharField(max_length=20)
    bprice = models.IntegerField()
    des = models.CharField(max_length=50)
    image = models.FileField(upload_to='bookapp/static/books')

class profilemodel(models.Model):
    cid = models.IntegerField()
    name=models.CharField(max_length=20)
    phn = models.IntegerField()
    loc = models.CharField(max_length=50)

class addcart(models.Model):
    bookname = models.CharField(max_length=20)
    bookprice = models.IntegerField()
    bookimage = models.FileField(upload_to='bookapp/static/cart')