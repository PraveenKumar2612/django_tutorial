from django.shortcuts import render

# Create your views here.

def net_demo(request):
    return render(request=request,template_name='main.html')