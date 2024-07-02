from django.urls import path
from django.http import HttpResponse
from recipes.views import _test, _home, _contacts


urlpatterns = [
    path('sobre/', _test),
    path('', _home),
    path('contacts/', _contacts),


]