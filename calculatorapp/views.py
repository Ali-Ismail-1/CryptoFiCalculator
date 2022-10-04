from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


@require_GET
def calc(request):
    print("In the calculate function")
    return HttpResponse('10')