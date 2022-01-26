from django.urls import re_path
from django.views.generic import ListView, DateDetailView

from blog.models import Post


app_name = 'blog'


urlpatterns = [
    re_path(
        r'^$',
        ListView.as_view(queryset=Post.objects.published(), paginate_by=3),
        name='post-list'),
    re_path(
        r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(date_field="publish", model=Post),
        name='post-detail')
]
