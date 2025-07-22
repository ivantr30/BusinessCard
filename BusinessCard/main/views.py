from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, template_name='main.html')
def contacts(request):
    return render(request, template_name='contacts.html')
def portfolio(request):
    return render(request, template_name='portfolio.html')
def applications(request):
    return render(request, template_name='applications.html')