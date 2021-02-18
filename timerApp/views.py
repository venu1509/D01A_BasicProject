from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def time_display(request):
    today=datetime.datetime.now()
    result="<H1> today is : "+str(today)
    return HttpResponse(result)