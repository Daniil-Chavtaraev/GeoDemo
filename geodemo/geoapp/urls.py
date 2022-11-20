from django.urls import path
from . import views

"""
registrating views
"""

urlpatterns = [
    path('', views.Home.as_view(), name="allsites"),
    path('site/<str:pk>/', views.Site.as_view(), name="site"),
    path('hazardform', views.CreateHazard.as_view(), name="hazardform"),
    path('allhazards', views.ListHazards.as_view(), name="allhazards"),
    path('hazard/<str:pk>/', views.Hazard.as_view(), name="hazard")
]