from django.conf.urls import include, re_path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    re_path(r'^$', views.api_root),
    re_path(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    re_path(r'^users/$', views.UserList.as_view(), name='user-list'),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
