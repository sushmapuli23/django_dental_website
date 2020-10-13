from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        treatment = request.POST['treatment']
        msg = request.POST['msg']

        send_mail(
            'Smile Ever Dental Team',
            'Thank you for Making an Appointment with us....feel free to contact if you have any queries',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
            )

        return render(request, 'home.html')

    else:
        return render(request, 'home.html')


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def gumsurgery(request):
    return render(request,'gumsurgery.html')

def generaldentistry(request):
    return render(request, 'generaldentistry.html')

def dentalimplant(request):
    return render(request, 'dentalimplant.html')

def periodontics(request):
    return render(request, 'periodontics.html')

def orthodontics(request):
    return render(request, 'orthodontics.html')

#@csrf_exempt

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        treatment = request.POST['treatment']
        msg = request.POST['msg']


        return render(request,"contact.html",{'name':name})


    else:
        return render(request,"contact.html",{})




#def contact(request):
    # if request.method == 'POST':
    #     contact = Contact()
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     date = request.POST.get('date')
    #     treatment = request.POST.get('treatment')
    #     msg = request.POST.get('msg')

    #     contact.name = name
    #     contact.email = email
    #     contact.date = date
    #     contact.treatment = treatment
    #     contact.msg = msg
    #     contact.save()
    #     return HttpResponse(" <h1>Thanks For Contacting Us</h1>")

    #return render(request, 'contact.html')
        
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from .models import Contact