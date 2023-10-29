from django.shortcuts import render,redirect
from django.utils import timezone
from .models import *
from .forms import *
from bs4 import BeautifulSoup
import requests
# Create your views here.

def home(request):
    data=timezone.now().date().weekday()
    weekday={
        '0':'Monday',
        '1':'Tuesday',
        '2':'Wednesday',
        '3':'Thursday',
        '4':'Friday',
        '5':'Sataurday',
        '6':'Sunday',
    }
    day=weekday[str(data)]
    d=breakfast.objects.get(dates=data)
    timer=times.objects.get(day=data)
    today3=str(timezone.now().year)
    today1=str(timezone.now().month)
    today2=str(timezone.now().day)
    today=f'{today3}-{today1}-{today2}'
    todaytasks=tasks.objects.all().filter(date=today)
    #web scrapping
    crickreq1=requests.get("https://m.cricbuzz.com/")
    jobreq2=requests.get("https://internshala.com/jobs/python-django-jobs/work-from-home/")
    soup1=BeautifulSoup(crickreq1.content,"html.parser")
    soup2=BeautifulSoup(jobreq2.content,"html.parser")
    cricketteam1 = soup1.find_all(class_='bat-team-scores')
    cricketteam2 = soup1.find_all(class_='ui-team2-scores')
    elements1 = soup2.find_all(class_='internship_meta')
    elements2 = soup2.find_all(class_='btn btn-secondary view_detail_button_outline')
    jobanchor=elements2[:5]
    jobprofile=elements1[:5]
    team1 = [element.text for element in cricketteam1]
    team2 = [element.text for element in cricketteam2]
    datas1 = [element.text for element in jobprofile]
    anchorjob=[element.get("href") for element in jobanchor ]
    
    jobdata=zip(datas1,anchorjob)
    crickdata=zip(team1,team2)
    
    
    
    dsa1 = Dataofdaily.objects.values_list('dsa', flat=True)
    project1=Dataofdaily.objects.values_list('project',flat=True)
    time1=Dataofdaily.objects.values_list('date',flat=True)
    dsa=list(dsa1)
    project=list(project1)
    days_of_month = [date.day for date in time1]
    
    
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
        'cricketdata':crickdata,
        'internshala_jobdata':jobdata,
        
        'DSA': dsa,
        'project':project,
        'dates':days_of_month
    }

    return render(request,'home.html',context)



def converter(value):
    a=int (value)
    choice = ['HPC','SE','DAA','CN','AI','BIG DATA','CN lab','DAA lab','No class']           
    return choice[a-1]




def addtask(request):
    if request.method =='POST':
        inputform=addtaskss(request.POST)
        if inputform.is_valid():
            inputform.save()
            return redirect('home')
    else:
        inputform=addtaskss()
    return render(request,'form.html',{'inputform':inputform})


def deletetask(request,uid):
    d=tasks.objects.filter(uid=uid)
    d.delete()
    return redirect('home')
