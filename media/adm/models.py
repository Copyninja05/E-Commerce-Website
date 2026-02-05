from django.db import models
from django.contrib.auth.models import User

# Create your models here.(

class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    descreption=models.TextField()
    image=models.ImageField(upload_to='products/')
    sections=models.CharField(max_length=20,choices=[('flash','flash sale'),
                                                     ('best','best selling'),
                                                     ('explore','Explore')])

    def __str__(self):
        return self.name
    

class whistle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(product, on_delete=models.CASCADE)


class contactdetails(models.Model):
    name=models.CharField(max_length=100)
    mobilenum=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name
    

class checkoutdetails(models.Model):
    fname=models.TextField(max_length=255)
    lname=models.TextField(max_length=255,null=True)
    street=models.TextField(max_length=255)
    apartment=models.TextField(max_length=255)
    city=models.TextField(max_length=255)
    number=models.CharField(max_length=15)
    email=models.TextField()

    def __str__(self):
        return self.fname


class add_to_cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return self.products.name
    