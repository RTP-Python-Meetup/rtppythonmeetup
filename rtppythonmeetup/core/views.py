from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePage(TemplateView):

    template_name = 'core/home.html'
