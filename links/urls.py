from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from links import views

urlpatterns = [
    url(r'^links/$', views.LinkList.as_view()),
    url(r'^links/(?P<pk>[0-9]+)/$', views.LinkDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)