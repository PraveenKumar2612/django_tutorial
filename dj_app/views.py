from django.shortcuts import render

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