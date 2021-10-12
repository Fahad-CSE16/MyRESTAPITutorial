from django.urls import path
from .views import *
from .registration import *

urlpatterns = [
    path('first/',firstAPI),
    path('registration/',registration),
]
