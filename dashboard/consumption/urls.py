from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.summary),
    url(r'^summary/', views.summary),
    url(r'^detail/(?P<UID>[0-9]+)', views.detail),
    #url(r'^detail/', views.detail),
]
