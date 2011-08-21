from django.conf.urls.defaults import * #patterns, include, url
from django.views.generic import ListView
from bookmarks.models import Bookmark

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'ffavourites.views.home', name='home'),
    # url(r'^ffavourites/', include('ffavourites.foo.urls')),
	url(r'^$','bookmarks.views.index',name='home'),
	
	url(r'^add','bookmarks.views.add'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
