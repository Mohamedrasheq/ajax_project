from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Profile
# Create your views here.
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
from django.http import JsonResponse
from .models import Profile  # Assuming you have a Profile model
from django.core.serializers import serialize

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']
        data = Profile(name=name, email=email, bio=bio)
        data.save()
        success='User '+name+' Created Successfully'
        return HttpResponse(success)
   

def getdata(request):
    if request.method=='GET':
        profiles=Profile.objects.all()
        serialized_profile=serialize('json',profiles)
        return JsonResponse(serialized_profile,safe=False)
def profile_view(request):
    return render(request,'data_fetch.html')

