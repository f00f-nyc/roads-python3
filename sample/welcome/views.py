from django.shortcuts import render
from django.views import generic


class WelcomeViewer(generic.TemplateView):
    template_name = 'index.html'

