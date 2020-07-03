from django.urls import path,include
from crud import views

urlpatterns = [
    path('home/',views.homeView, name="home"),
    path('home/show/',views.showView),
    path('submit/',views.submit, name='submit'),
]