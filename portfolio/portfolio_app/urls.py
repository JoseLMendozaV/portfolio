from django.urls import path
from django.urls.resolvers import URLPattern
from portfolio_app import views

app_name = 'portfolio_app'

urlpatterns = [
    path('', views.index, name='index'),
]