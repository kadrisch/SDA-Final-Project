from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import TextForm
from .logic import punctuation_removal, text_upper

class IndexPage(FormView):
    template_name = 'index.html'
    form_class = TextForm
    success_url = reverse_lazy('guide')

    def form_valid(self, form):
        global form_data
        form_data = form.cleaned_data
        return super().form_valid(form)


def GuidePage(request):
    changed_data = {}
    text = form_data['textarea']
    latest_text = text
    if bool(form_data['remove_punctuations']):
        changed_data['Remove Punctuations:'] = punctuation_removal(text)
        latest_text = punctuation_removal(latest_text)
    if bool(form_data['upper_case']):
        changed_data['Upper Case:'] = text_upper(latest_text)
        latest_text = text_upper(latest_text)
    context = {
        'latest_text': latest_text,
        'content': changed_data
    }
    return render(request, template_name='guide.html', context=context)
