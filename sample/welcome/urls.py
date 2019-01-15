from django.conf.urls import include, url
from welcome.views import WelcomeViewer


urlpatterns = [
    url(r'^', WelcomeViewer.as_view(), name="welcome_home"),
]

