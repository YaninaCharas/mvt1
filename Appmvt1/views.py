from django.shortcuts import render
from Appmvt1.models import Familia
from _datetime import datetime

def listafamilia(request):
    integrante1 = Familia(nombre="Tobias", edad=23, email="pp@gmail.com", fnac=datetime.now())
    integrante2 = Familia(nombre="Agustin", edad=20, email="pp@gmail.com", fnac=datetime.now())
    integrante3 = Familia(nombre="Fabian", edad=52, email="pp@gmail.com", fnac=datetime.now())

    integrante1.save()
    integrante2.save()
    integrante3.save()

    contexto = {"persona1": integrante1, "persona2": integrante2, "persona3": integrante3}

    return render(request, "webfamiliar.html", contexto)

