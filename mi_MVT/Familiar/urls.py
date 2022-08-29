from calendar import c
from django.urls import path
from .views import ver_familiar

urlpatterns = [
    path('familiar/', ver_familiar, name ="familiar")
]
