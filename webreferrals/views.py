from django.views.generic import TemplateView
from django.db.models import F
from links.models import Link

class LinksView(TemplateView):
    template_name = "links.html"

class LandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        slug = self.request.GET.get('link')
        link = Link.objects.filter(slug=slug)
        if link.count() > 0:
            link.update(clicks=F('clicks') + 1)
            context['message'] = "You've reached the " + slug + " landing page!"
        else:
            context['message'] = "You're on the default landing page."
        return context