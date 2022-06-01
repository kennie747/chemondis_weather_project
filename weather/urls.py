"""weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from weather import views

# from django.urls import include
# # from froala_editor import views
# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from weather.views import *

handler404 = 'weather.views.custom_page_not_found_view'
handler500 = 'weather.views.custom_error_view'
handler403 = 'weather.views.custom_permission_denied_view'
handler400 = 'weather.views.custom_bad_request_view'

urlpatterns = [
    path('home_cached/', views.home_cached),
    path('', views.home),
    path('home/', views.home),
    path('admin/', admin.site.urls),
    path('weather/search', views.search), 
    path('config/', views.configuration), 
    path('config/save_config', views.save_config),
    path('weather/', views.weather),
    path('i18n/', include('django.conf.urls.i18n')),
    
]
