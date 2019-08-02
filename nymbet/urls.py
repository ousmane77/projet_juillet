from django.urls import path
from .views import home, match, championnat, documentation

app_name = 'nymbet'


urlpatterns = [
    path('', home, name='home'),
    path("match/<int:id>", match, name='match'),
    path("championnat/<int:id>", championnat, name='championnat'),
    path("documentation", documentation, name='documentation'),

]
