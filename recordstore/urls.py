from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from store import views

urlpatterns = [
    url(r'^$',views.home_view),
    url(r'^store/', include(('store.urls','store'),namespace ='store')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + urlpatterns