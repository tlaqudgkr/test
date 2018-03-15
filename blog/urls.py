from django.conf.urls import url
from blog.views import BlogListView, BlogDetailView, BlogUpdateView, BlogCreateView, BlogDeleteView, GameListView, GameDetailView

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='bloglist'),
    url(r'^(?P<pk>\d+)/$', BlogDetailView.as_view(), name='blogdetail'),
    url(r'^(?P<pk>\d+)/update/$', BlogUpdateView.as_view(), name='blogupdate'),
    url(r'^new$', BlogCreateView.as_view(), name='blogcreate'),
    url(r'^(?P<pk>\d+)/delete$', BlogDeleteView.as_view(), name='blogdelete'),

    url(r'^$', GameListView.as_view(), name='gamelist'),
    url(r'^detail/$', GameDetailView.as_view(), name='gamedetail'),
]