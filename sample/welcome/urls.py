from django.conf.urls import patterns, url
from welcome.views import WelcomeViewer


urlpatterns = patterns(
    "",
    url(r"^$", WelcomeViewer.as_view(), name="welcome_home"),
)
