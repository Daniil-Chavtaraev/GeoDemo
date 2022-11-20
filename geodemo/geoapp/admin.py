from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Hazard, Site

"""
setting 
"""

@admin.register(Hazard)
class HazardAdmin(OSMGeoAdmin):
    list_display = ('title', 'point')

@admin.register(Site)
class SiteAdmin(OSMGeoAdmin):
    list_display = ('title', 'polygon')

# Register your models here.
