import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^data/$', views.DataPageView.as_view(), name='data'),
    url(r'^data/search/$', views.get_search_results, name='search_results'),
    url(r'^data/search/(?P<search_query>[\w\-]+)/$', views.get_search_results, name='search_results'),
    url(r'^data/search/(?P<search_query>[\w\-]+)/(?P<page>[0-9]+)/$', views.get_search_results, name='search_results'),
    url(r'^data/details/(?P<app_id>[0-9]+)/$', views.get_
