from django.urls import path
from . import views

urlpatterns = [
    path('pelicula/crear/', views.crear_recomendacion_pelicula, name = 'crear_recomendacion_pelicula'),
    path('documental/crear/', views.crear_recomendacion_documental, name = 'crear_recomendacion_documental'),
    
    path('serie/crear/', views.crear_recomendacion_serie, name = 'crear_recomendacion_serie'),
    path('series/buscar/', views.busqueda_series, name = 'busqueda_series'),
    path('series/lista_series', views.lista_series, name = 'lista_series'),
    path('serie/borrar/<int:id>/', views.borrar_recomendacion_serie, name = 'borrar_recomendacion_serie'),
    path('serie/actualizar/<int:id>/', views.actualizar_recomendacion_serie, name = 'actualizar_recomendacion_serie'),
    
    path('peliculas/', views.PeliculasLista.as_view(), name = 'lista_peliculas'),
    path('peliculas/<int:pk>/', views.PeliculaDetalle.as_view(), name = 'detalle_pelicula'),
    path('peliculas/<int:pk>/editar/', views.PeliculaEditar.as_view(), name = 'editar_pelicula'),
    path('peliculas/<int:pk>/borrar/', views.PeliculaBorrar.as_view(), name = 'borrar_pelicula'),
    
]
