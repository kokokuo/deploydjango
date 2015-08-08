from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deploydjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'deploydjango.views.home'),
    url(r'^home/$', 'deploydjango.views.home'),
    url(r'^deployapp/home/$', 'deployapp.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)
