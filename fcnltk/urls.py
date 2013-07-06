from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^lista/$', views.lista, name='lista'),
    url(r'^ngramas/$', views.ngramas, name='ngramas'),
    url(r'^(?P<called_path>\w+)/\w+$', views.front_controller, name='front_controller'),
    # Examples:
    # url(r'^$', 'fcnltk.views.home', name='home'),
    # url(r'^fcnltk/', include('fcnltk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
