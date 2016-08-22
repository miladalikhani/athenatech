from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup', views.singup, name='signup'),
    url(r'^login', views.login, name='login'),
    url(r'^test', views.test_get, name='test_get'),
    url(r'^receive', views.receive, name='receive'),
    url(r'^get_login', views.get_login, name='loginGet'),
]