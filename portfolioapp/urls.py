from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('/qulification', views.qulification,name='qulification'),
    path('experince', views.experince,name='experince'),
    path('/community',views.community,name='community'),
    path('save_email/', views.save_email, name='save_email'),
]