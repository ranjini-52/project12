from django.shortcuts import render

# Create your views here.
def goodmorning(request):
    return render(request,'goodmorning.html')
   