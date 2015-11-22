from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from ops.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ops_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index,name='index'),
    url(r'^saltcmd/$', saltcmd,name="saltcmd"),
    url(r'^saltlog/$', saltlog,name="saltlog"),
    url(r'^saltscp/$', saltscp,name="saltscp"),
    url(r'^saltscript/$', saltscript,name="saltscript"),
    url(r'^cmd$', cmd,name="cmd"),
    url(r'^status/$', status,name="status"),
    url(r'^server_asset/$', server_asset,name="server_asset"),
    url(r'^network_device_asset/$', network_device_asset,name="network_device_asset"),
)
