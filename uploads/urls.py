from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('order_pizza/', views.order_pizza, name='order_pizza'),

    url('contact/', views.contact, name='contact'),
]
