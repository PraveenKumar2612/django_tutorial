from django.shortcuts import render

def custom_error(request,exception):
    return render(request=request,template_name='custom_error.html')