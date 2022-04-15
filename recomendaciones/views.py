from ast import Delete
from django.shortcuts import redirect, render

from . models import Series, Peliculas, Documentales
from . forms import SerieFormulario, PeliculaFormulario, SerieBusqueda, DocumentalFormulario
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def crear_recomendacion_serie(request):
    
    if request.method == 'POST':
        form = SerieFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            serie = Series(nombre = data['nombre'], categoria = data['categoria'], netflix = data['netflix'] )
            serie.save()
            return redirect('lista_series') 
            
    form = SerieFormulario()
    return render(request, 'recomendaciones/crear_recomendacion_serie.html', {'form' : form})


def crear_recomendacion_pelicula(request):
       
    if request.method == 'POST':
        form = PeliculaFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            serie = Peliculas(nombre = data['nombre'], categoria = data['categoria'], netflix = data['netflix'] )
            serie.save()
            return redirect('index') 
            
    form = PeliculaFormulario()
    return render(request, 'recomendaciones/crear_recomendacion_pelicula.html', {'form' : form}) 


def crear_recomendacion_documental(request):
           
    if request.method == 'POST':
        form = DocumentalFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            serie = Documentales(nombre = data['nombre'], categoria = data['categoria'], netflix = data['netflix'] )
            serie.save()
            return redirect('index') 
            
    form = DocumentalFormulario()
    return render(request, 'recomendaciones/crear_recomendacion_documental.html', {'form' : form}) 


def busqueda_series(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        series = Series.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        series = Series.objects.all()
    
    form = SerieBusqueda()
    return render(request, 'recomendaciones/busqueda_series.html', {'form': form, 'series': series})


#CRUD

def lista_series(request):
    lista_series = Series.objects.all() 
    return render(
        request, 'recomendaciones/lista_series.html',
        {'lista_series': lista_series}
    )
    
def actualizar_recomendacion_serie(request, id):
    
    serie = Series.objects.get(id = id)
    
    if request.method == 'POST':
        form = SerieFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            serie.nombre = data['nombre']
            serie.categoria = data['categoria']
            serie.netflix = data['netflix']
            serie.save()
            return redirect('lista_series') 
            
    form = SerieFormulario(
        initial = {
            'nombre': serie.nombre,
            'categoria': serie.categoria,
            'netflix': serie.netflix
        })
    return render(
        request, 'recomendaciones/actualizar_recomendacion_serie.html',
        {'form' : form, 'serie': serie}
    )    

def borrar_recomendacion_serie(request,id):
    serie = Series.objects.get(id = id)
    serie.delete()
    return redirect('lista_series')


#CRUD CON CBV

class PeliculasLista(LoginRequiredMixin,ListView):
    model = Peliculas
    template_name = 'recomendaciones/lista_peliculas.html'
    
    
class PeliculaDetalle(DetailView):
    model = Peliculas
    template_name = 'recomendaciones/datos_peliculas.html'
    
    
class PeliculaEditar(UpdateView):
    model = Peliculas
    success_url = '/recomendaciones/peliculas/'
    template_name = 'recomendaciones/editar_pelicula.html'
    fields = ['nombre', 'categoria', 'netflix']
    
    
class PeliculaBorrar(DeleteView):
    model = Peliculas
    success_url = '/recomendaciones/peliculas/'
    template_name = 'recomendaciones/borrar_pelicula.html'
    

class PeliculaCrear(CreateView):
    model = Peliculas
    success_url = '/recomendaciones/pelicula/crear/'
    template_name = 'recomendaciones/crear_recomendacion_pelicula.html'
    fields = ['nombre', 'categoria', 'netflix']  
     