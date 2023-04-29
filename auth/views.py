from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from gfg import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str

# from . tokens import generate_token 
from django.core.mail import EmailMessage,send_mail





# Create your views here.
def home(request):
    return render(request , "auth/index.html")



def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username')
         username = request.POST['username']
         fname = request.POST['fname']
         lname = request.POST['lname']
         email = request.POST['email']
         pass1 = request.POST['pass1']
         pass2 = request.POST['pass2']
        
         if User.objects.filter(username = username):
             messages.error(request,"Username already Exist! Please Choose another Username")
             return redirect('home')
         
         if User.objects.filter(email = email):
             messages.error(request," Email Already Exist")
             return redirect('home')
         
         if len(username)>10:
             messages.error(request, "Username cannot be greater than 10 charaters")


         if pass1 != pass2:
             messages.error(request,"Passowrd Didn't Match")
         

         if not username.isalnum():
             messages.error(request, "Username shoud be Alpha-numeric")
             return redirect('home')




         myuser = User.objects.create_user(username,email,pass1)
         myuser.first_name = fname
         myuser.last_name = lname
        #  myuser.is_active = False
         myuser.save()

         messages.success(request,"Your account has been successfully created ! \n We have sent you a welcome mail ! \n Enjoy our services ")

         #Weclome email
         subject = "Welcome to CU FoOD - Your Ultimate Food Ordering Destination!"
         message = "Dear "+ myuser.first_name + "!! \n\n"+"Welcome to CU FoOD, your go-to destination for ordering delicious meals online. As a college student, we know how hectic life can be, and that's why we're here to make things easier for you. Our platform offers a variety of food options that cater to your taste buds and dietary preferences.\n\nOur menu includes pizzas, burgers, sandwiches, wraps, salads, and more, all from local restaurants and food joints. You can order from the comfort of your home or dorm, and we'll take care of the rest.\n\n To get started, simply visit our website [insert website link here] and browse our menu. Once you find what you want, place your order, and enjoy the food. \n\n Thank you for choosing CU FoOD for all your food ordering needs. We can't wait to serve you!\n\nBest regards,\nThe CU FoOD Team"
         
         
         
         
         
         
         from_email = settings.EMAIL_HOST_USER
         to_list = [myuser.email]

         send_mail(subject, message,from_email,to_list,fail_silently = True)


        #Email address confirmation Email

        #  current_site = get_current_site(request)
        #  email_subject = "Confirm your email @ CU Food Login!"
        #  message2 = render_to_string('email_confirmation.html',{
        #      'name':myuser.first_name,
        #      'domain':current_site.domain,
        #      'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
        #      'token': generate_token.make_token(myuser)
        #  })
        #  email = EmailMessage(
        #      email_subject,
        #      message2,
        #      settings.EMAIL_HOST_USER,
        #      [myuser.email],
        #  )
        #  email.fail_silently = True
        #  email.send()
        #  return redirect('signin')




    return render(request, 'auth/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']


        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request, "auth/index.html",{'fname':fname})
        else:
            messages.error(request,"UID/Password is Worng please try again!")
            return redirect('home')





    return render(request, 'auth/signin.html')

def signout(request):
   logout(request)
#    messages.success(request,"Logged Out Successfully")
   return redirect('home')


def about(request):
   
   return render(request,'auth/about.html')


# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk = uid)
#     except(TypeError,ValueError,OverflowError,User.DoesNotExist):
#         myuser = None
#     if myuser is not None and generate_token.check_token(myuser,token):
#         myuser.is_active = True
#         myuser.save()
#         login(request,myuser)
#         return redirect('home')
#     else:
#         return render(request,'activation_failed.html')




# photo - file
# photo - photo-> bytes - bytes stream to mongodb
# s3 - aws buckets - integrate