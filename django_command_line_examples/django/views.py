from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import ListForm , TutorialsForm
def home(request):
    form = ListForm()
    return render(request,'app/home.html',{'form':form})
def about(request):

    return render(request,'app/about.html')
def addTutorial(request):
    if request.method == 'POST':
        form = TutorialsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TutorialsForm()


    return render(request,'app/add_tutorial.html',{'form':form})
