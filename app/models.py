from django.db import models
from django.core import validators
import uuid

# Create your models here.
class breakfast(models.Model):
    food1 =models.CharField(max_length=100,default="null")
    drink1=models.CharField(max_length=100,default="null")
    
    
    dates=models.IntegerField(default=2,validators=[
            validators.MinValueValidator(0, message='Value must be greater than or equal to 0'),
            validators.MaxValueValidator(6, message='Value must be less than or equal to 6'),
        ])
    
    
    food2 =models.CharField(max_length=100,default="null")
    drink2=models.CharField(max_length=100,default="null")
    

    food3 =models.CharField(max_length=100,default="null")
    drink3=models.CharField(max_length=100,default="null")
    
    
    food4 =models.CharField(max_length=100,default="null")
    drink4=models.CharField(max_length=100,default="null")
    
class times(models.Model):
    choice = [
    ('1', 'HPC'),
    ('2', 'SE'),
    ('3', 'DAA'),
    ('4', 'CN'),
    ('5', 'AI'),
    ('6', 'BIG DATA'),
    ('7', 'CN lab'),
    ('8', 'DAA lab'),
    ('9', 'null'),
        ]
    eight=models.CharField(max_length=40,choices=choice,default='9',name="eight")
    nine=models.CharField(max_length=40,choices=choice,default='9',name="nine")
    ten=models.CharField(max_length=40,choices=choice,default='9',name="ten")
    eleven=models.CharField(max_length=40,choices=choice,default='9',name="eleven")
    twelve=models.CharField(max_length=40,choices=choice,default='9',name="twelve")
    one=models.CharField(max_length=40,choices=choice,default='9',name="one")
    two=models.CharField(max_length=40,choices=choice,default='9',name="two")
    three=models.CharField(max_length=40,choices=choice,default='9',name="three")
    four=models.CharField(max_length=40,choices=choice,default='9',name="four")
    five=models.CharField(max_length=40,choices=choice,default='9',name="five")
    day=models.IntegerField(validators=[
            validators.MinValueValidator(0, message='Value must be greater than or equal to 0'),
            validators.MaxValueValidator(6, message='Value must be less than or equal to 6'),
        ])
    
    
class tasks(models.Model):
    uid =models.UUIDField(default=uuid.uuid4,editable=False)
    todo=models.CharField(max_length=100,default="null")
    date=models.DateField(auto_now=False, auto_now_add=False)