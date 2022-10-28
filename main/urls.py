from django.urls import path

from main.views import *

urlpatterns = [
    path('categories/', get_categories),
    path('services/', get_services),
    path('services/<str:text>/', get_services_for_title),
    path('salons/', get_salons),
    path('auto/', get_json_autos),
    path('services_apiview/', ServicesApiView.as_view()),
]