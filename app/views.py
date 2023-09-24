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
    today3=str(timezone.now().year)
    today1=str(timezone.now().month)
    today2=str(timezone.now().day)
    today=f'{today3}-{today1}-{today2}'
    todaytasks=tasks.objects.all().filter(date=today)
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
        'time2':converter(timer.nine),
        'time3':converter(timer.ten),
        'time4':converter(timer.eleven),
        'time5':converter(timer.twelve),
        'time6':converter(timer.one),
        'time7':converter(timer.two),
        'time8':converter(timer.three),
        'time9':converter(timer.four),
        'time10':converter(timer.five),
        'task':todaytasks,
    }
    return render(request,'home.html',context)



def converter(value):
    a=int (value)
    choice = ['HPC','SE','DAA','CN','AI','BIG DATA','CN lab','DAA lab','no class']           
    return choice[a-1]





