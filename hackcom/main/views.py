#TODO: level 1 - Recognising current status of mental health and provide steps accordingly to prevent problems ML model to predict Mental degradation and provide steps accordingly
#TODO: A portal where therapists and people can sign up and people can book appointments with therapists
#TODO: UI - A autism, color blindness, epilepsy friendly
#TODO: Think and ideate for level 2 - software support for fighting mental health
#TODO: If time, implement dashboard
#TODO: Some js logic in Login page and Signup Page


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .models import form, therapist
from geopy.geocoders import Nominatim
from django.core.mail import send_mail

# Create your views here.
def homepage(request):
	if request.user.is_authenticated:
		user = User.objects.get(id=request.user.id)
		return render(request, "home.html", {'user':user})	
	return render(request, "home.html")

def loginPage(request):
	if request.method == 'POST':
		post = request.POST
		uname = post['username']
		if User.objects.filter(username=uname):
			user = User.objects.filter(username=uname)[0]
			if user.check_password(post['pass']):
				login(request, user=user)
				return redirect('/')
			else:
				return render(request, 'login.html', {'pas':'Password is incorrect'})
		else:
			return render(request, 'login.html', {'usr':'User dosent exist'})
	else:
		if request.user.is_authenticated:
			return redirect('/')
		return render(request,'login.html')

def meds(request):
	if not request.user.is_authenticated:
		return redirect("/login")
	return render(request, 'meditation.html')

def signup(request):
	if request.method == 'POST':
		post = request.POST
		uname = post['username']
		name = post['name']
		if User.objects.filter(username=uname):
			return render(request,'signup.html', {'usr':'Username already exists'})
		if post['pass1'] != post['pass2']:
			return render(request,'signup.html', {'pas':'Passwords do not match'})
		user = User.objects.create_user(username=uname, first_name=name, email=post['email'], password=request.POST['pass1'])
		return redirect('/login')
	else:
		return render(request,'signup.html')

def LogoutPage(request):
	logout(request)
	return redirect('/')

def FormPage(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	if request.method=='POST':
		post=request.POST
		user = User.objects.get(id=request.user.id)
		form.objects.create(user=user, age=post['age'], Gender=post['gender'], family_history=post['fam_hist'], benefits=post['benefits'],care_options=post['care'],anoymity=post['anoymity'],leave=post['leave'], work_interfere=post['work_interfere'])
	return render(request, 'form.html')


def signuptherapist(request):
	if request.method == 'POST':
		post = request.POST
		uname = post['username']
		name = post['name']
		if User.objects.filter(username=uname):
			return render(request,'therapistSignup.html', {'usr':'Username already exists'})
		if post['pass1'] != post['pass2']:
			return render(request,'therapistSignup.html', {'pas':'Passwords do not match'})
		user = User.objects.create_user(username=uname, first_name=name, email=post['email'], password=request.POST['pass1'])
		thera = therapist.objects.create(user=user,age=post['age'],Gender=post['sex'],field=post['field'],number=post['Number'],pin=post['pincode'],address=post['address'],from_time=post['from'],to_time=post['to'])
		return redirect('/login')
	else:
		return render(request,'therapistSignup.html')


def therapistContact(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	geolocator = Nominatim(user_agent="geoapiExercises")
	pincode = 390003
	therapists = therapist.objects.all()
	'''
	location = geolocator.geocode(pincode, addressdetails=True)
	user_location = location.raw['address']['state_district']
	available = []
	available_user = []
	for x in therapists:
		location = geolocator.geocode(x.pin, addressdetails=True)
		print(location.raw['address']['state_district'])
		if location.raw['address']['state_district'] == user_location:
			available.append(x)
			'''
	return render(request, 'TherapistView.html',{'therapist':therapists})

def profile(request,uname):
	if not request.user.is_authenticated:
		return redirect('/login')
	if request.method == 'POST':
		request.user.first_name
		user =User.objects.get(username=uname)
		send_mail(
    	'New Appointment',
    	f'{request.user.first_name} just booked an appointment with you!',
    	'automated.aadil@gmail.com',
    	[f'{user.email}'],
    	fail_silently=True,
		)
		return render(request,'profile.html',{'user':User.objects.get(username=uname), 'therapist':therapist.objects.get(user=User.objects.get(username=uname)), 'success':True})
	if not User.objects.filter(username=uname):
		return HttpResponse('404 Not Found')
	if not therapist.objects.filter( user=User.objects.get(username=uname)):
		return HttpResponse('404 Not Found')
	return render(request,'profile.html',{'user':User.objects.get(username=uname), 'therapist':therapist.objects.get(user=User.objects.get(username=uname)), 'success':False})

def pomodoro(request):
	if not request.user.is_authenticated:
		return redirect("/login")
	return render(request,'pomodoro.html')