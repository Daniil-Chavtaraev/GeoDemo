from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView
from django.core.serializers import serialize
from . import models
from . import forms

class Home(ListView):
    """
    view for main page
    lists all sites
    """
    model = models.Site
    template_name = 'geoapp/allsites.html'
    context_object_name = 'sites'

class Site(DetailView):
    """
    view for detail site view
    serializing data to geojson
    """
    model = models.Site
    template_name = 'geoapp/site.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        pk = self.kwargs.get('pk')
        context['polys'] = serialize('geojson', self.model.objects.filter(pk=pk),
                  geometry_field='polygon')
        context['hazardpoints'] = serialize('geojson', models.Hazard.objects.all(),
                  geometry_field='point')
        # context['polys'] = self.model.objects.get(pk=pk)
        print(context['hazardpoints'])
        return self.render_to_response(context)

class CreateHazard(CreateView):
    """
    view for creation form for hazards
    """
    form_class = forms.HazardForm
    template_name = 'geoapp/hazardform.html'

class ListHazards(ListView):
    """
    view for hazards page
    lists all hazards
    """
    model = models.Hazard
    template_name = 'geoapp/allhazards.html'
    context_object_name = 'hazards'

class Hazard(DetailView):
    """
    view for detail hazard view
    serializing data to geojson
    """
    model = models.Hazard
    template_name = 'geoapp/hazard.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        pk = self.kwargs.get('pk')
        context['pts'] = serialize('geojson', self.model.objects.filter(pk=pk),
                  geometry_field='point')
        # context['polys'] = self.model.objects.get(pk=pk)
        print(context['pts'])
        return self.render_to_response(context)