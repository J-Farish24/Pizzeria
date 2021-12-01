from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    #Home page for pizzeria website
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all().order_by('name')

    context = {'pizzas': pizzas}

    return render(request, 'pizzas/pizzas.html', context)