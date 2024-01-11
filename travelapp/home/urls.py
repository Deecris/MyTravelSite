from django.urls import path

from travelapp.home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home_page')
]