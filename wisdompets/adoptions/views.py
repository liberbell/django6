from django.shortcuts import render
from django.http import HttpResponse

from .models import Pet
# Create your views here.
def home(request):
    pets = Pet.objects.all()
    # return HttpResponse('<p>home view</p>')
    return render(request)

def pet_detail(request, id):
    return HttpResponse('<p>pet_detail view with the id {}</p>'.format(id))
