from django.shortcuts import render,redirect
from .models import *
from .forms import *

def homeView(request):
    surveyData.objects.all().delete()
    form = surveyForm()

    if request.method == 'POST':
        form = surveyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('show/')
    return render(request, 'home.html',{'form':form})

def showView(request):
    all_data = surveyData.objects.all()
    return render(request,'show.html',{'all_data':all_data})
    
def submit(request):
    return render(request, 'submit.html')