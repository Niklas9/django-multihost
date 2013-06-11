from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django_multihost.views.multihost1'),
)
