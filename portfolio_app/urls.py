from django.urls import path
from django.urls.resolvers import URLPattern
from portfolio_app import views
from .views import IndexView

app_name = 'portfolio_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]