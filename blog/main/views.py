# Create your views here.
from django.http import HttpResponse
from main.models import Category

def home(request):
    cats = Category.objects.all()
    return HttpResponse(cats)