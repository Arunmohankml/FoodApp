from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class CustomUser(AbstractUser):
    roles=(
        ('hotel', "Hotel owner"),
        ('manager', "Hotel manager"),
        ('user', "Normal user")
    )
    role=models.CharField(choices=roles, default='user',max_length=15)

class Hotels(models.Model):
    owner = models.CharField(default='none', max_length=30)
    name=models.CharField(default='none',max_length=30)
    location=models.CharField(default='other',max_length=30)
    image=models.FileField(upload_to='items/shops/',default='default.jpg')
    bio=models.CharField(default='',max_length=100)
    RATING_CHOICES = [
        (0, '0 Stars'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    rating=models.IntegerField(choices=RATING_CHOICES, default=0)
    time = models.JSONField(default=dict, blank=True, null=True)
    email = models.EmailField(default='', max_length=100)
    number1=models.CharField(default='',max_length=13)
    number2=models.CharField(default='',max_length=13)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, related_name='managed_hotels')
    
    def __str__(self):
        return f"{self.name}"
    
class Sections(models.Model):
    name=models.CharField(default='other',max_length=30)
    def __str__(self):
        return f"{self.name}"

class Items(models.Model):
    name=models.CharField(default='other',max_length=30)
    image=models.FileField(upload_to='shopitems/',default='default.jpg') 
    section = models.ForeignKey('Sections', on_delete=models.CASCADE, default=1)
    def __str__(self):
        return f"{self.name}"
    
class ShopItems(models.Model):
    hotel = models.ForeignKey('Hotels', on_delete=models.CASCADE, default=1, related_name='shop_items')
    name=models.CharField(default='other',max_length=30)
    image=models.FileField(upload_to='items/shops/',default='default.jpg')
    section = models.ForeignKey('Sections', on_delete=models.CASCADE, default=1)
    type = models.ForeignKey('Items', on_delete=models.CASCADE, default=1)
    desc=models.CharField(default='',max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    RATING_CHOICES = [
        (0, '0 Stars'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    rating=models.IntegerField(choices=RATING_CHOICES, default=0)
    def __str__(self):
        return f"{self.name}"
    