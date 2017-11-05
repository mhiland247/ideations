from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
#from registration import views

urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page'),
    url(r'contact/$', views.contact_post, name='contact_post'),
    #url(r'^accounts/login/$', auth_views.login),
    #url(r'^accounts/logout/$', auth_views.logout),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^main/$', views.main_page, name='main_page'),
]
