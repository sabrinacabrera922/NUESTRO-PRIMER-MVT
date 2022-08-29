from django.shortcuts import render
from .models import Familiar

# Create your views here.
def home(request):
      return render(request, "home.html", context={})

def ver_familiar(request):
    familiar = Familiar.objects.create(name = "Pedro", telefono=6655147, fecha_nacimiento="1990-5-10")
    familiar1 = Familiar.objects.create(name = "Alberto" , telefono=5454884, fecha_nacimiento="1992-2-11")
    familiar2 = Familiar.objects.create(name = "Johana" , telefono=5454884, fecha_nacimiento="1988-1-27") 
    context = {
        'familiar': familiar,
        'familiar1': familiar1,
        'familiar2': familiar2} 
    return render(request, 'home.html', context)   