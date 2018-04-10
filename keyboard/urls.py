from django.conf.urls import include,url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
]
