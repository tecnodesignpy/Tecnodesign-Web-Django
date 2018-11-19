from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^send-email/', views.send_email),
    url(r'^404/', views.error404),
    url(r'^sumate/', views.jobs),
    url(r'^$', views.website),
]