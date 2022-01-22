from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing_album_view),
]