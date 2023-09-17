from django import urls
from django.contrib import admin
from django.urls import path
from django.urls import include
from portfolio_app import views
from django.conf import settings
from django.conf.urls.static import static
from portfolio_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio_app/', include('portfolio_app.urls')),
    path('jnfgk5849hjfgkdfldj394kj2k2kgj5rt33/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)