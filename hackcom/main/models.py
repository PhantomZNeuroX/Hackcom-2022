from django.db import models
from django.contrib.auth.models import User

class form(models.Model):
    WORK = [
        ('Never', 'Never'),
        ('Often', 'Often'),
        ('Rarely', 'Rarely'),
    ]
	
    LEAVE = [
        ('SE', 'Somewhat easy'),
        ('DK', "Don't know"),
        ('SD', 'Somewhat difficult'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=20)
    family_history = models.BooleanField(null=True)
    benefits = models.BooleanField(null=True)
    care_options = models.BooleanField(null=True)
    anoymity = models.BooleanField(null=True)
    leave = models.CharField(choices=LEAVE, null=True, max_length=4)
    work_interfere = models.CharField(choices=WORK, null=True, max_length=8)
    complete = models.BooleanField(null=True, default=False)

class therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=20)
    field = models.CharField(max_length=20)
    number = models.CharField(max_length=12)
    pin = models.IntegerField(null=False)
    address = models.TextField(max_length=150)
    from_time = models.CharField(max_length=50)
    to_time = models.CharField(max_length=50)