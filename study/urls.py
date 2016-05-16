from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.study, name='study'),
    # url(r'^(?P<category_slug>[-\w]+)/$', views.shop, name='product_index_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]