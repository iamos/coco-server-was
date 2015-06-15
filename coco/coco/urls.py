from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'users.views.sign_up'),
    url(r'^signup/$', 'users.views.sign_up', name='sign_up'),
    url(r'^login/$', 'users.views.login', name='login'),
    url(r'^logout/$', 'users.views.logout'),
    url(r'^dashboard/', 'dashboard.views.index'),
    url(r'^posts/', include('posts.urls')),
]
