# home/urls.py
from django.conf.urls import url ,include

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/', views.AboutPageView.as_view(), name='about'),
    url(r'fform/', views.first_form, name='fform'),
    url(r'fform/submited', views.submited, name='fform_submited'),
]