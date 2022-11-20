import json
from pathlib import Path
from geoapp.models import Site
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, Polygon
# sites = Path(r'C:\Users\quilt\PycharmProjects\GeoDemo1.6\geodemo\geoapp\management\commands\sites.json')

sites = Path(__file__).absolute()
sites = list(sites.parts)
sites[len(sites) - 1] = 'sites.json'
sites = Path(*sites).absolute()


class Command(BaseCommand):

    help = "Parsing data from sites.json to postgres"

    def handle(self, *args, **options):
        """
        Opning .json file and parsing it, pushing it into postgres

        """
        with open(sites, 'r') as file:
            rawfile = json.load(file)
            for elem in rawfile:
                title: str = elem.get('title')
                form_parse = Site()
                form_parse.title = title
                poly = Polygon(tuple([tuple(item) for item in elem.get('points')]))
                form_parse.polygon = GEOSGeometry(poly)
                form_parse.save()
