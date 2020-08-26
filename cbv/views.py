from django.views.generic.base import TemplateView
from cbv.models import Post

class Ex2View(TemplateView):
    
    template_name = "ex2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "Context Data for Ex2"
        return context