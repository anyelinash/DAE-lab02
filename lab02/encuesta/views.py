from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def calcular(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operacion = request.POST['operacion']
        resultado = None

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2

        return render(request, 'encuesta/resultado.html', {'resultado': resultado, 'num1': num1, 'num2': num2, 'operacion': operacion})

    return render(request, 'encuesta/calculadora.html')

def resultado(request):
    return render(request, 'encuesta/resultado.html')

def calvolumen(request):
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        radio = diametro / 2
        volumen = 3.14159265359 * radio * radio * altura

        return render(request, 'encuesta/restcilindro.html', {'volumen': volumen, 'altura': altura, 'diametro': diametro})

    return render(request, 'encuesta/cilindro.html')