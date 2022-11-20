from django.contrib.gis.forms import OSMWidget
from django.forms import forms, ModelForm
from . import models

class HazardForm(ModelForm):
    """
    creating form with redirect to root page
    """
    class Meta:
        model = models.Hazard
        widgets = {'point': OSMWidget(attrs={'default_lat':32, 'default_lon':35})}
        fields = ['title', 'point']