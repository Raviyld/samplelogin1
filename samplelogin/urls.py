from django.conf.urls import patterns, include, url
from login import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'samplelogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^login/$', views.login),
    (r'^EditProfile/$', views.EditProfile),
    (r'^EditProfile_fun/(?P<id>\d+)/$', views.EditProfile_fun),
    (r'^Registration/$', views.Registration),
    url(r'^admin/', include(admin.site.urls)),
)
