from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

__author__ = 'Derek Stegelman'
__date__ = '11/3/12'

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('apps.project.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:

    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += staticfiles_urlpatterns()