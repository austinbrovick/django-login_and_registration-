from django.conf.urls import patterns, url
from . import views
urlpatterns = patterns('',
  url(r'^register/$', views.Register.as_view(), name='accounts-register'),
  url(r'^login/$', views.Login.as_view(), name='accounts-login'),
  url(r'^success/$', views.Success.as_view()),
)
