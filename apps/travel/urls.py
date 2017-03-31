from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.index, name="index"),
	url(r'^show$', views.show, name="show"),
	url(r'^show/(?P<id>\d+)$', views.show, name="show"),
	url(r'^join$', views.join, name="join"),
	url(r'^add$', views.add, name="add"),
	url(r'^add_travel$', views.add_travel, name="add_travel"),
	
	]