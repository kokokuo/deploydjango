from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deploydjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'deploydjango.views.home'),
    url(r'^home/$', 'deploydjango.views.home'),
    url(r'^deployapp/home/$', 'deployapp.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)


# Custion 404 views and page
handler404 = 'deploydjango.views.error404'
# Custion 500 views and page
handler500 = 'deploydjango.views.error500'


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, documment_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)