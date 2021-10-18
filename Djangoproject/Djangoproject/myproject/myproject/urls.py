"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from django.urls import path
from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
from django.urls import path

urlpatterns = [
    path('<int:start_year>/<int:start_month>/<int:start_day>/<int:start_hour>/<int:start_min>/<int:start_sec>/<int:end_year>/<int:end_month>/<int:end_day>/<int:end_hour>/<int:end_min>/<int:end_sec>/sec_results/', views.sec_results, name='sec_results'),
    path('<int:start_year>/<int:start_month>/<int:start_day>/<int:end_year>/<int:end_month>/<int:end_day>/sec_results_date/', views.sec_results_date, name='sec_results_date'),

    url(r'^admin/', admin.site.urls),
    url(r'^timediff_response', views.timediffout.as_view()),
    path('', views.index, name='index'),
    
   
   
]
