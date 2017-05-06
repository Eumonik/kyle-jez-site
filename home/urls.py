from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .models import Post, Tag, Category

urlpatterns = [
    url(r'^robots.txt$', TemplateView.as_view(template_name="home/robots.txt", content_type="text/plain"), name="robots_file"),
    url(r'^$', views.HomeView.as_view(), name = 'home'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^blog/$', views.PostListView.as_view(), name = 'posts'),
    url(r'^blog/search/', include('haystack.urls')),
    url(r'^blog/categories/$', views.CategoriesListView.as_view(), name = 'categories'),
    url(r'^blog/categories/([a-z]+)/', views.CategorysListView.as_view(), name = 'category'),
    url(r'^blog/tags/$', views.TagListView.as_view(), name = 'tags'),
    url(r'^blog/tags/([a-z0-9]+)/$', views.TagsListView.as_view(), name = 'tag'),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name = 'post'),


]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    url(r'^blog/archives/$', ArchiveIndexView.as_view(model = Post, date_field = "posted"), name = 'archives'),
    url(r'^blog/archives/(?P<pk>[0-9]+)/', views.ArchiveDetailView.as_view(), name = 'archive'),
'''

'''
url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        ArticleMonthArchiveView.as_view(month_format='%m'),
        name="archive_month_numeric"),



    url(r'^blog$', views.blog, name = 'blog'),
    url(r'^blog/.', views.post),
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-posted")[:5],
        template_name='home/base.html')),
    url(r'^blog', ListView.as_view(
        queryset=Post.objects.all().order_by("-posted")[:25],
        template_name="cheese")),
'''
