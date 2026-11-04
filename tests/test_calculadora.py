import pytest

from calculadora import dividir, fatorial, multiplicar, somar, subtrair


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(2, 3) == -1


def test_multiplicar():
    assert multiplicar(4, 3) == 12


def test_dividir():
    assert dividir(7, 2) == 3.5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(1, 0)


@pytest.mark.parametrize("n, esperado", [(0, 1), (1, 1), (5, 120)])
def test_fatorial(n, esperado):
    assert fatorial(n) == esperado


@pytest.mark.parametrize("n", [-1, 2.5])
def test_fatorial_invalido(n):
    with pytest.raises(ValueError):
        fatorial(n)
