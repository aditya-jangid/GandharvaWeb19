#inlcude the various features which are to be used in Views here
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from EventApp.models import Department, EventMaster, Carousel, SponsorMaster, RoleAssignment, RoleMaster, MyUser, EventDepartment
from .forms import UserRegistration , ContactUsForm, RoleMasterForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from EventApp.decorators import user_Role_head

# Create your views here.


#Home page Functionality
def home(request):

    args = {
        'events': Department.objects.all(),
        'sponsors': SponsorMaster.objects.all(),
        'carouselImage': Carousel.objects.all(),
        'gandharvaDate': 'March 20, 2019'
    }

    return render(request, 'gandharva/index.html', args)

#Events page of all Departments
def event(request):
    if request.POST:
        dept = request.POST.get('dept')
        dept_choose = Department.objects.get(name=dept)
    else:
        dept = 'All Events'
    args1 = {
        'pageTitle': dept,
        'events': EventDepartment.objects.filter(department = dept_choose),
    }
    return render(request, 'events/event1.html', args1)

#Details of Individual Events
def details(request):
    event_name = request.POST.get('event')

    arg = {
        'events_list': EventMaster.objects.all(),
        'pageTitle': EventMaster.objects.get(event_name__startswith=event_name).event_name,
        'event': EventMaster.objects.get(event_name__startswith=event_name),
       # Temperorily rules are disabled
       # 'rules': EventMaster.objects.get(event_name__startswith=event_name).rules.split('. '),
    }
    return render(request, 'events/category1Event1.html', arg)

#ContactUs View (Form created)
def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus')
        else:
            print(form.errors)
    else:
        form = ContactUsForm()

    return render(request, 'gandharva/contactus.html',{'form':form})

#Registration for normal User and log in user after registration Immediately
def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            login(request, user, backend='social_core.backends.google.GoogleOAuth2')
            return redirect('home')
        else:
            print (form.errors)

    else:
        form = UserRegistration()

    return render(request, 'events/register.html', {'form': form})

#logout Option View appears only after login
def user_logout(request):
        logout(request)
        return redirect('home')

#Login for user to Existing Account
def user_login(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('home')
                    else:
                        print("Your account was inactive.")
            else:
                messages.error(request, 'Error wrong username/password')
                return render(request, 'events/login.html', {})

        else:
            return render(request, 'events/login.html', {})

def payment (request):
    return render(request, 'user/paymentDetails.html', {})

#Head Login View only to be used for Heads
@user_passes_test(lambda u: u.is_superuser)
def RegisterHead(request):
    Roles = RoleMaster.objects.all();
    if request.method == 'POST':
        userform = UserRegistration(request.POST)
        roleform = RoleMasterForm(request.POST)
        if userform.is_valid() and roleform.is_valid():
            user = userform.save()
            username = userform.cleaned_data.get('username')
            password = userform.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            roleassign = RoleAssignment()
            roleassign.user=user
            roleassign.role = roleform.cleaned_data.get('name')
            roleassign.save()
      #       group = Group.objects.get(name='groupname')
      #      user.groups.add(group)
      #login(request, user, backend='social_core.backends.google.GoogleOAuth2')
            return redirect('home')
        else:
            print (userform.errors)
            print (roleform.errors)


    else:
        userform = UserRegistration()
        roleform = RoleMasterForm

    return render(request, 'events/RegisterHead.html', {'userform': userform , 'roleform': roleform, 'roles':Roles})




## Important Notes:
# to get user role from models
 #userget = RoleAssignment.objects.get(user=request.user.id)
 #   print (userget.role)


