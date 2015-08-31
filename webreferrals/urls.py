from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'webreferrals.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^links', include('links.urls')),
    url(r'^landing/?$', views.LandingView.as_view()),
    url(r'^/?$', views.LinksView.as_view())
]
