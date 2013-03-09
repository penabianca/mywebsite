from django.conf.urls.defaults import patterns, include,url

urlpatterns = patterns('website.views',
    url(r'^add','add')
    )
