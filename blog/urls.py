from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list.html, name='post_list')
]
