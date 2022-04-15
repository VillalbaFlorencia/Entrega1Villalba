from django import forms


class SerieFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    netflix = forms.BooleanField(required = False)
    descripcion = forms.CharField(max_length=50, required= False)
    
    
class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    netflix = forms.BooleanField(required = False)
    
    
class DocumentalFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    netflix = forms.BooleanField(required = False)


class SerieBusqueda(forms.Form):
    nombre = forms.CharField(max_length=30)
    