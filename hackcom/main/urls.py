from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login', views.loginPage),
    path('signup', views.signup),
    path('logout',views.LogoutPage),
    path('form',views.FormPage),
    path('therapist/signup',views.signuptherapist),
    path('therapist/search',views.therapistContact),
    path('profile/<uname>',views.profile),
    path('meditation',views.meds),
    path('pomodoro',views.pomodoro)
]
