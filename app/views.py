from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime

from app.forms import ClientForm

def horario_atual(request):
    horario_atual = datetime.datetime.now()
    # return HttpResponse(horario_atual)
    return render(request,'mostra_horario.html', context={'horario': horario_atual})

def form_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('form_ok')
    form = ClientForm()
    return render(request, 'form_client.html', context={'form':form})

def form_ok(request):
    return render(request, 'form_ok.html', context={'form_ok': form_ok})