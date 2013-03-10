from django.conf.urls.defaults import patterns, include,url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#..rest of url.py config...
urlpatterns += patterns('website.views',
    url(r'^add','add')
    )
