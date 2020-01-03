from django.shortcuts import render
from . import models

# Create your views here.


def all_moneybooks(request):

    all_moneybooks = models.Moneybook.objects.all()
    return render(request, "moneybooks/home.html", context={"all_moneybooks": all_moneybooks})
