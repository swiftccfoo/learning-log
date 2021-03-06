# defines URL patterns for learning_logs

from django.conf.urls import include, url
from django.contrib.auth.views import login

from . import views

urlpatterns = [

    # login page
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),

    # Home page
    url(r'^$', views.index, name = 'index'),

    # Show all topics
    url(r'^topics/$', views.topics, name = 'topics'),

    # detail page for a single topic
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),

    # page for adding new topic
    url(r'^new_topic/$', views.new_topic, name = 'new_topic'),

    # page for adding new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
