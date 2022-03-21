from django.urls import path
from . import views

urlpatterns = [
    path('serie/crear/', views.crear_recomendacion_serie, name = 'crear_recomendacion_serie'),
    path('pelicula/crear/', views.crear_recomendacion_pelicula, name = 'crear_recomendacion_pelicula'),
    path('documental/crear/', views.crear_recomendacion_documental, name = 'crear_recomendacion_documental'),
    path('series', views.lista_series, name = 'lista_series')
]
