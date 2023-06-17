from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('login/',views.log,name='logpage'),
    path('register/',views.register,name='registerpage'),
    path('logout/',views.logout),
    path('about',views.about,name='aboutpage')
]