#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
#from mysite.views import hello, current_datetime, hours_ahead
#from mysite.books import views
from django.contrib import admin
admin.autodiscover()

	#(?P<name>pattern)
urlpatterns = patterns('mysite.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # practice
    url('^$', 'hello'),
    url('^hello/$', 'hello'),
    url('^time/$', 'current_datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),

    #url(r'^search_form/$', search_form),
    #url(r'^search/$', search),
)

urlpatterns += patterns('mysite.books.views',
    url(r'^search_form/$', 'search_form'),
    url(r'^search/$', 'search'),

)

urlpatterns += patterns('mysite.contact.views',
    url(r'^contact/$', 'contact'),

)
