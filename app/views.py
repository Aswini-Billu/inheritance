from django.shortcuts import render

# Create your views here.
def aswini(request):
    return render(request,'parent.html')

def sandy(request):
    return render(request,'child.html')
