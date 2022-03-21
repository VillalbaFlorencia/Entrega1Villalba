from django.shortcuts import redirect, render

from . models import Series, Peliculas, Documentales
from . forms import SerieFormulario, PeliculaFormulario, DocumentalFormulario, SerieBusqueda

# Create your views here.

def crear_recomendacion_serie(request):
    
    if request.method == 'POST':
        form = SerieFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            serie = Series(nombre = data['nombre'], categoria = data['categoria'], netflix = data['netflix'] )
            serie.save()
            # return render(request, 'index/index.html', {})
            return redirect('index') 
            
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


def lista_series(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        series = Series.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        series = Series.objects.all()
    
    form = SerieBusqueda()
    return render(request, 'recomendaciones/lista_series.html', {'form': form, 'series': series})