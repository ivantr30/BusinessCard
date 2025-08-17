from django.shortcuts import render
from .forms import ApplicationForm

# Create your views here.
def main(request):
    return render(request, template_name='main.html')
def contacts(request):
    return render(request, template_name='contacts.html')
def portfolio(request):
    return render(request, template_name='portfolio.html')
def applications(request):
    msg = ""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Success"
        else:
            msg = "Maboy, the form is not valid"
    else:
        form = ApplicationForm()
    return render(request, template_name='applications.html', context={'form': form, 'msg' : msg})