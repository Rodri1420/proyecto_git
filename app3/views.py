from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el mas capo</h1>")

def pagina3(request):
    html="""
        <h1 style="color:blue">Hola app2</h1>
        <p>Soy el cra de la app2.</p>
    """

    return HttpResponse(html)