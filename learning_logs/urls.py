# defines URL patterns for learninig_logs

from django.conf.urls import include, url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name = 'index'),

    # Show all topics
    url(r'^topics/$', views.topics, name = 'topics'),

    # detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
]
