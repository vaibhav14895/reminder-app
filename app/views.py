from django.shortcuts import render
from django.utils import timezone
from .models import *
# Create your views here.

def home(request):
    data=timezone.now().date().weekday()
    weekday={
        '0':'monday',
        '1':'tuesday',
        '2':'wednesday',
        '3':'thursday',
        '4':'friday',
        '5':'sataurday',
        '6':'sunday',
    }
    day=weekday[str(data)]
    d=breakfast.objects.get(dates=data)
    timer=times.objects.get(day=data)
    context={
        'day':day,
        'breakfast':d.food1,
        'breakfastdrink':d.drink1,
        'lunch':d.food2,
        'lunchdrink':d.drink2,
        'evening':d.food3,
        'eveningdrink':d.drink3,
        'dinner':d.food4,
        'dinnerdrink':d.drink4,
        'time1':converter(timer.eight),
        'time2':timer.nine,
        'time3':timer.ten,
        'time4':timer.eleven,
        'time5':timer.twelve,
        'time6':timer.one,
        'time7':timer.two,
        'time8':timer.three,
        'time9':timer.four,
        'time10':timer.five,
    }
    return render(request,'home.html',context)



def converter(value):
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
    for a in choice:
        if value==choice[a]:
          time=choice[a]
    
    print(value)
    return time





