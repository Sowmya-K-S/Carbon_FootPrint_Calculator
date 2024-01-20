from django.shortcuts import render,redirect,HttpResponse
from user.models import *
from user.models import User_Details

from random import randint
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    global c_otp
    # when we click on register option
    if request.method == 'GET':
        return render(request, 'register.html')
    
    # when we click on register button
    else:
       
        # checking whether the entered email is already used for registration
        try:
            # error occurs when there is no email match
            # then control goes to except block

            global user_details 
            user_details=User_Details.objects.get(email = request.POST['email'])
            return render(request,'register.html',{'msg':"Email already registered, try using other Email"})
        
        except:
            # validating password and confirm password
            if request.POST['password'] == request.POST['confirmpassword']:
                #  generating otp
                global c_otp
                c_otp = randint(100_000,999_999)

                #extracting data from registration form
                global reg_form_data 

                reg_form_data = {
                    "name" : request.POST['name'],
                    "email" : request.POST['email'],
                    "password" : request.POST['password'],
                    "confirmpassword" : request.POST['confirmpassword']
                    
                }

                # sending the generated OTP via mail
                subject = "OTP Verification"
                message = f'Hello{reg_form_data["name"]}, Welcome to Pixel Perfect. Your OTP is {c_otp}'
                sender = settings.EMAIL_HOST_USER
                receiver = [reg_form_data['email']]
                send_mail(subject, message, sender, receiver)

                #after sending OTP render the page to enter OTP
                return render(request,'otp.html')

            else:
                return render(request, 'register.html',{'msg':"Both Passwords didn't match"})
            
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            # finding the record of person trying to login in database
            session_user = User_Details.objects.get(email = request.POST['email'])
            if request.POST['password'] == session_user.password:
                request.session['email'] = session_user.email
                return redirect('index')
            else:
                return render(request, 'login.html', {'msg':'invalid password'})
        except:
            return render(request, 'login.html',{'msg': 'This email is not Registered !!'})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def calculator(request):
    return render(request,'calculator.html')

def otp(request):
    if str(c_otp) == request.POST['u_otp']:
        User_Details.objects.create(name=reg_form_data['name'], email = reg_form_data['email'],password = reg_form_data['password'])
        return render(request,'register.html', {'msg': "Registration Successfull !! Account created"})
    else:
        return render(request, 'otp.html',{'msg':"Invalid OTP"})


def discover(request):
    return render(request,'discover.html')