from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
class CustomUser(AbstractUser):
    # Add any additional fields you need here
    pass



class PanditProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    speciality = models.CharField(max_length=255)
    dob = models.DateField()
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name