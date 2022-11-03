from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from index.forms import TextArea, Response


def hello(request):
    content = 'Hello world! I am learning django!'

    return HttpResponse(content)


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TextArea
        return context


class GuidePage(TemplateView):
    template_name = 'guide.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
