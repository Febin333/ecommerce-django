from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from store.models import Customer

# Create your views here.
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = User.objects.create_user(username=username, password=password,
                                                email=email)
        customer=Customer.name='username'
        customer = Customer.email = 'email'
        customer.save()

        if password!=cpassword:
            messages.info(request,"password not matched")
        # elif User.objects.filter(username=username).exists():
        #     messages.ino(request,"username taken")
        else:
            user.save()
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']
     user=auth.authenticate(username=username,password=password)
     if user is not None:
         auth.login(request,user)
         return redirect('/')
     else:
         messages.info(request,'invalid username or password')
    return render(request,'login.html')