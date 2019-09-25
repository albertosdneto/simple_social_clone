from django.views.generic import TemplateView

class TestePage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'



class HomePage(TemplateView):
    template_name = 'index.html'