"""
Definition of models.
"""

from django.db import models

# Create your models here.


class ContactForm(models.Model):
    regards =(
        ('Real Estate','Real Estate'),
        ('Mortgage','Mortgage'),
        ('Event Hall','Event Hall'),
        )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(max_length=500)
    regards = models.CharField(max_length=10, choices=regards)
    

class HomeListing(models.Model):
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    description = models.TextField(max_length=500)
    sqft = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    picture1 = models.ImageField(upload_to='images/')
    picture2 = models.ImageField(upload_to='images/', blank=True, null=True)
    picture3 = models.ImageField(upload_to='images/', blank=True, null=True)
    picture4 = models.ImageField(upload_to='images/', blank=True, null=True)
    picture5 = models.ImageField(upload_to='images/', blank=True, null=True)
