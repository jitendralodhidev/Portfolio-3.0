from django.shortcuts import render
from django.http import  HttpResponse
from .models import Contact
from.models import Feedback
# from .models import Contact
# Create your views here.



def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')


def contact(request):
    
    if request.method == "POST":

            name = request.POST ['name']
            email = request.POST ['email']
            phone = request.POST ['phone']
            desc = request.POST ['desc']
            if name =='' or email == '' or phone == '' or desc == '':
                print("data is Blank")
            else:

                 ins = Contact(name=name,email=email,phone=phone,desc=desc)
                 ins.save()
                 print("data saved")

                    

    return render(request,'contact.html')

def feedback(request):
    if request.method == "POST":
            comment = request.POST.get('comment','default')
            suggest = request.POST.get('suggest','default')
            name = request.POST ['name']
            email = request.POST ['email']
            phone = request.POST ['phone']
            desc = request.POST ['desc']
            if name =='' or email == '' or phone == '' or desc == '':
                print("data is Blank")
            else:
                ins = Feedback(name=name,email=email,phone=phone,desc=desc,comment=comment,suggest=suggest)
                ins.save()
                print("feedback saved")

            
            

    return render(request,'feedback.html')

# def certificates(request):
#     return HttpResponse('this is certificates page ')
#
# def resume(request):
#     return HttpResponse('this is resume page ')