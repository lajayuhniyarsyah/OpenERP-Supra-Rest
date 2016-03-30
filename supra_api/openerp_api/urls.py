from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from openerp_api import views
 
urlpatterns = patterns('',
  url(r'^openerp-login/$', views.CustomGet.as_view()),
  # url(r'^openerp/(?P<model>[a-zA-Z,.]+)/$', views.ServiceModel.as_view()),
   url(r'^openerp/(?P<model>[a-zA-Z,.]+)/$',views.GetModel),
    # url(r'^openerp/getjason/$',views.asdsd),
   # url(r'^json/$',views.json),
   url(r'^openerp/(?P<model>[a-zA-Z,.]+)/(?P<mode>(search|ids|getupdate|jsonrpc))/$',views.GetModel),
)
 
urlpatterns = format_suffix_patterns(urlpatterns)