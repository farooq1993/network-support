from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages


from django.http import HttpResponse
from .models import Student, Wireless
from .forms import StudentForm, WirelessForm


def submit_student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # create a new Student object with the form data
            new_student = Student(
                name=form.cleaned_data['name'],
                course_name=form.cleaned_data['course_name'],
                roll_number=form.cleaned_data['roll_number'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number']
            )
            # save the new student object to the database
            new_student.save()
            # redirect to a success page
            return redirect('submit_student_form')
    else:
        form = StudentForm()
    return render(request, 'student_registration_form.html', {'form': form})



def wireless(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        ipaddress=request.POST['ipaddress']
        transportprotocol=request.POST['transportprotocol']
        #transport_protocol=transportprotocol.objects.get(id=id)
        wir=Wireless(username=username, password=password, ipaddress=ipaddress, transportprotocol=transportprotocol)
        wir.save()

        return redirect("login")
    # context={
    #     "transport_protocol":transport_protocol
    # }
    return render(request, "wireless.html")

        
        # else:
   
            
    
    # context={
    #     "form":form
    # } 
    

def Login(request):
    if request.method == "POST":
        username=request.POST['username']
        
        password=request.POST['password']

        transportprotocol=request.POST['transportprotocol']
        #transport_protocol=transportprotocol.objects.get(id=id)
        wir=Wireless(username=username, password=password,transportprotocol=transportprotocol)
        wir.save()
        
        user=authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print("------", user)
            return redirect('function_generatore')
        # else:
        #    messages.info(request, 'Invalid Username or Password')
        #    return redirect('/') 
    
    return render(request,"wireless.html")

def fungenerate(request):
    if request.method == 'POST':        
        ipaddress=request.POST['ipaddress']
        transportprotocol=request.POST['transportprotocol']
        wir=Wireless(ipaddress=ipaddress, transportprotocol=transportprotocol)
        wir.save()

        return redirect("home")
    # context={
    #     "transport_protocol":transport_protocol
    # }
    return render(request, "functi-generat.html")


def home(request):
    return render(request, 'mainpage.html')


def Logout(request):
    logout(request)
    return redirect("wireless")



def get_data(request):
    if request.method=='POST':
        search=request.POST['transportprotocol']
        wire2=Wireless.objects.filter(transportprotocol__icontain=search)
    return render(request, 'function-generat.html', {"wire2":wire2})
