from django.shortcuts import render, redirect
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


def deletevoter(request, id):
    deletee = Registration.objects.get(id=id)
    deletee.delete()
    return redirect('/viewvoters')


def editvoter(request, id):
    object = Registration.objects.get(id=id)
    context = {'context': object}
    return render(request, 'updatevoter.html', context)


def updatevoter(request, id):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        national_ID = request.POST.get('National_ID')
        county = request.POST.get('County')

        updatee = Registration.objects.get(id=id)
        updatee.Name = name
        updatee.Email = email
        updatee.Phone = phone
        updatee.National_ID = national_ID
        updatee.County = county
        updatee.save()
    return redirect('/viewvoters')
