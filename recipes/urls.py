from django.urls import path
from recipes.views import _home


urlpatterns = [
    path('', _home),
]