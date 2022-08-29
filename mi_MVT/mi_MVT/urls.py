from django.contrib import admin
from django.urls import path
from Familiar.views import home, ver_familiar#, crear_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('familiar/',ver_familiar)#,
    #path('familiar/', crear_familiar)
]
