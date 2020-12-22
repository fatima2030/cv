from django.shortcuts import render

# Create your views here.

def home_view(request):
    context={}

    return render(request,'index.html',context)

def details(request):
    context={}

    return render(request,'portfolio-details.html',context)

def blogdetails(request):
    context={}

    return render(request,'blog.html',context)


def covid(request):
    context={}

    return render(request,'covid.html',context)

def tiwtter(request):
    context={}

    return render(request,'tiwtter.html',context)



def delivery(request):
    context={}

    return render(request,'delivery.html',context)
