from django.conf.urls import patterns, include, url
from poll_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^(?P<poll_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<poll_id>[0-9]+)/vote$', views.vote, name='vote'),
	url(r'^registration/', views.registration, name='registration'),
	url(r'^signin/', views.signin, name='signin'),
	url(r'^signout/', views.signout, name='signout'),
	url(r'^(?P<poll_id>[0-9]+)/delete/', views.delete, name='delete'),

)