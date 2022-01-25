from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing_album_view, name="listing"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail_album_view, name="detail"),
    url(r'^search/$', views.search_album_view, name="search"),
]
