"""
This code should be copied and pasted into blog/urls.py
"""


from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    ## add your url here
)
