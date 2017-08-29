from django.shortcuts import render
from django.viewer import generic


class WelcomeViewer(generic.TemplateView):
    template_name = "index.html"

