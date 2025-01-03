from django.shortcuts import render
from dj_app.models import Users

# Create your views here.

def net_demo(request):
    top_movies_list=[
        {
        "cardbodytext":"this is image 2",
        "cardimg":'images/pic 2.jpeg'
    },
        {
        "cardbodytext":"this is image 3",
        "cardimg":'images/pic 3.jpeg'
    },
        {
        "cardbodytext":"this is image 4",
        "cardimg":'images/pic 4.jpeg'
    },
        {
        "cardbodytext":"this is image 5",
        "cardimg":'images/pic 5.jpeg'
    },
        {
        "cardbodytext":"this is image 6",
        "cardimg":'images/pic 6.jpeg'
    },
    #     {
    #     "cardbodytext":"this is image 2",
    #     "cardimg":'images/pic 2.jpeg'
    # },
    #     {
    #     "cardbodytext":"this is image 3",
    #     "cardimg":'images/pic 3.jpeg'
    # },

    ]
    
    data={
       "content":top_movies_list
    }
    return render(request=request,template_name='main.html',context=data)

def index_view(request):
    data={
        "scentance":"the modulation of h1 tag in html",
        "img_url":'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0mo1-1RPPCSd54lH3fcOeOWM1wRHxEZ3C1A&s'
    }
    return render(request=request,template_name='index.html',context=data)

def about_us(request):
    return render(request=request,template_name='aboutus.html')

def login_id(request):
    print('sucess')
    return render(request=request,template_name='login.html')

def home_page(request):
    print(request.POST['user_id'])
    user=Users(user_id=request.POST['user_id'],password=request.POST['password'])
    user.save()

    data={
        "user_id":request.POST['user_id'],
        "password":request.POST['password']
    }
    return render(request=request,template_name='home.html',context=data)

def orm(request):
    return render(request=request,template_name='home.html')

