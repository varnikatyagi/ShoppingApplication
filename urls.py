from django.urls import path
from . import views

#so when we import a module that module  will end up being an object so we can use . to access the function inside it



urlpatterns = [
    #in this list we can map various url to their view functions
    path('',views.index),
    path('new',views.new)
    #I'm not calling a function I'm simply passing a refrence to it
    #in this module we map the root url to this function
   
]
