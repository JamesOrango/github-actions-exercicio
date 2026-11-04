"""Calculadora simples usada no exercício de GitHub Actions."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("divisão por zero")
    return a / b


def fatorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n deve ser um inteiro não negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
