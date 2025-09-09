from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ProjectModel
from .forms import ApplicationForm

import requests
import os

# Create your views here.
def main(request):
    return render(request, template_name='main.html')
def contacts(request):
    return render(request, template_name='contacts.html')
def portfolio(request):
    projects = ProjectModel.objects.all()
    return render(request, template_name='portfolio.html', context={'projects' : projects})
def applications(request):
    msg = ""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Success"
            data = form.cleaned_data
            message = (
                f"!Новая заявка:!\n"
                f"Имя: {data['name']}\n"
                f"Email: {data['email']}\n"
                f"Предложение: {data['offer']}"
            )
            send_offer(message)
            return HttpResponseRedirect("")
        else:
            msg = "Maboy, the form is not valid"
    else:
        form = ApplicationForm()
    return render(request, template_name='applications.html', context={'form': form, 'msg' : msg})
def send_offer(message):
    url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
    payload = {"chat_id": os.getenv('CHAT_ID'), "text": message}
    requests.post(url, json=payload)