from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import TextForm
from .logic import punctuation_removal, text_upper, text_lower, remove_new_line, remove_extra_space, count_characters, spell, wiki, remove_stop_words


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
    if bool(form_data['lower_case']):
        changed_data['Lower Case:'] = text_lower(latest_text)
        latest_text = text_lower(latest_text)
    if bool(form_data['new_line_remove']):
        changed_data['New Line Remove'] = remove_new_line(latest_text)
        latest_text = remove_new_line(latest_text)
    if bool(form_data['extra_space_remove']):
        changed_data['Extra Space Remove'] = remove_extra_space(latest_text)
        latest_text = remove_extra_space(latest_text)
    if bool(form_data['count_characters']):
        changed_data['Count Characters'] = count_characters(latest_text)
        latest_text = count_characters(latest_text)
    if bool(form_data['spell_check']):
        changed_data['Spell Check'] = spell(latest_text)
        latest_text = spell(latest_text)
    if bool(form_data['generate_word_summary']):
        changed_data['Generate Summary of a Word'] = wiki(latest_text)
        latest_text = wiki(latest_text)
    if bool(form_data['remove_stop_words']):
        changed_data['Remove Stop Words of Your Paragraph'] = remove_stop_words(latest_text)
        latest_text = remove_stop_words(latest_text)
    context = {
        'latest_text': latest_text,
        'content': changed_data
    }
    return render(request, template_name='guide.html', context=context)
