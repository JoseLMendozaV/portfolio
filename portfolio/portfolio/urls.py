from django import urls
from django.contrib import admin
from django.urls import path
from django.urls import include
from portfolio_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio_app/', include('portfolio_app.urls')),
    path('admin/', admin.site.urls),
]
