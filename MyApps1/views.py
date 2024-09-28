from django.shortcuts import render


# Create your views here.
def homepage_view(request):
    return render(request, 'ThirdApp/index.html')

def portfolio_view(request):
    return render(request, 'ThirdApp/portfolio-details.html')

def service_view(request):
    return render(request, 'ThirdApp/service-details.html')

def starter_view(request):
    return render(request, 'ThirdApp/starter-page.html')

def Maintain_view(request):
    return render(request, 'ThirdApp/Maintaince.html')
