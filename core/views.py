from django.shortcuts import render, HttpResponse

# Create your views here.


def somas(request, valor1, valor2):
    result = valor1+valor2
    return HttpResponse('<h1>soma = {}</h1>'.format(result))


def subtracao(request, valor1, valor2):
    result = valor1-valor2
    return HttpResponse('<h1>sub = {}</h1>'.format(result))


def multi(request, valor1, valor2):
    result = valor1*valor2
    return HttpResponse('<h1>multiplicacao = {}</h1>'.format(result))


def divi(request,  valor1, valor2):
    result = valor1/valor2
    return HttpResponse('<h1>divisao = {}</h1>'.format(result))


def mari(request):
    return HttpResponse('<h1>MARI EU TE AMO</h1>')
