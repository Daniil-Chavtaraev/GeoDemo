from django.db import models

from django.contrib.gis.db import models

class Site(models.Model):
    """
    model for Site with polygon area
    """
    title = models.CharField(max_length=100)
    polygon = models.PolygonField(geography=True)


    def __str__(self):
        return self.title

class Hazard(models.Model):
    """
    model for hazard with point
    """
    title = models.CharField(max_length=100)
    point = models.PointField(geography=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return ('/')

# Create your models here.
