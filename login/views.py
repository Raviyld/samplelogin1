from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,HttpResponseRedirect
from django.template.loader import get_template
from django.db import connection
from login.models import *
# from django.conf.urls.defaults import *
from django.contrib.auth import authenticate, login, logout
   
def login(request):
    uname = request.POST['uname']
    pwd = request.POST['pwd']
    print "Login views", uname, pwd
    try:
        m = User.objects.get(Username = request.POST['uname'], Password = request.POST['pwd'])
    except:
        return render_to_response('Registration.html',{'msg':'Please provide correct username and password'})
    print "m values",m.Username
    if (User.objects.get(Username__exact=request.POST['uname'], Password__exact = request.POST['pwd'])):
        un = User.objects.get(id__exact = m.id).Username
        Loginlog(Username=m).save()
        dt = Loginlog.objects.filter(Username=m).latest('Logindate')
        list = Loginlog.objects.filter(Username=m).all()
        print "list values un", un
        ep = User.objects.filter(Username=un).all()
        print "\n user details", ep
        d = User.objects.get(id__exact = m.id).DOB
        s = d.strftime("%m/%d/%Y")
        print "date is", s
        return render_to_response('EditProfile.html', {'msg':'Login is Success', 'list':list, 'uname':un,'dt':dt, 'ep':ep,'id':m.id,'DOB':s})
    else:
        return render_to_response('Registration.html', {'msg':'Login is Failure'})
    
 
def Registration(request):
    return render_to_response('Registration.html')
    
def EditProfile(request):
    username = request.POST['uname']
    pwd = request.POST['pwd'] 
    dob = request.POST['dob'] 
    gender = request.POST['gender'] 
    mobile = request.POST['mobile'] 
    mail = request.POST['mail']
    print "Add Registration page:", username, gender
    s = User(Username=username,Password=pwd,DOB=dob, Gender=gender, Mobile=mobile,Mail=mail)
    print 's', s.Username
    s.save()
    m = User.objects.filter(Username = s.Username).latest('Username')
    print "m values", m.id
    un = User.objects.get(id__exact = m.id).Username
    Loginlog(Username=m).save()
    dt = Loginlog.objects.filter(Username=m).latest('Logindate')
    list = Loginlog.objects.filter(Username=m).all()
    print "list values", list
    return render_to_response('EditProfile.html', {'msg':'Login is Success','list':list, 'username':username,'pwd':pwd,'dob':dob,'gender':gender,'mobile':mobile,'mail':mail, 'uname':un, 'dt':dt, 'id':m.id})
   
def EditProfile_fun(request,id):
    editprofile = User.objects.get(id = id)
    print "editprofile", editprofile
    if request.method == 'POST':
        username = request.POST['uname']
        pwd = request.POST['pwd'] 
        dob = request.POST['dob'] 
        gender = request.POST['gender'] 
        mobile = request.POST['mobile']
        mail = request.POST['mail']
        editprofile.Username = username
        editprofile.Password = pwd
        editprofile.DOB = dob
        editprofile.Gender = gender
        editprofile.Mobile = mobile
        editprofile.Mail = mail
        editprofile.save()    
        return render_to_response('Registration.html',{'msg':'Profile Updated succesfully'}) 
    else:  
        return render_to_response('Registration.html',{'msg':'Profile Update is failure'})