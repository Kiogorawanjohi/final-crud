from django.shortcuts import render,redirect
from .models import Registration
from .forms import RegistrationForm
def addvoter(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/viewvoters')
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})


def viewvoters(request):
    objects = Registration.objects.all()
    form = RegistrationForm()
    return render(request, 'registration.html', {'objects': objects, 'form': form})


def home(request):
    return render(request, 'home.html')


def deletevoter(request,pk):
    object=Registration.objects.get(id=pk)
    object.delete()
    return redirect('/viewvoters')


def editvoter(request,pk):
    object=Registration.objects.get(id=pk)
    form = RegistrationForm(request.POST, instance=object)
    if form.is_valid():
        form.save()
        return redirect('/viewvoters')
    return render(request, 'registration.html', {'form': form})
# Create your views here.

