from django.db import models

# Create your models here.
class Signup(models.Model):
    FirstName = models.CharField(max_length= 122)
    LastName = models.CharField(max_length= 122)
    Email = models.CharField(max_length= 122)
    Address = models.CharField(max_length= 122)
    PaymentMethod = models.CharField(max_length= 122)

    def __str__(self):
        return self.FirstName +' '+ self.LastName

class Cart(models.Model):
    Iphone = models.CharField(max_length=60)
    Space = models.CharField(max_length=60)
    Price = models.IntegerField()
    Total = models.IntegerField()

    