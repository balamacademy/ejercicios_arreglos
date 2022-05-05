from pytest import approx
import arreglos as arr

def test_mayores_que_1():
    assert arr.mayores_que(5, [7, 3, 6, 0, 4, 5, 10]) == 3

def test_mayores_que_2():
    assert arr.mayores_que(2, [-1, 1, 8, 2, 0]) == 1

def test_media_aritmetica():
    assert arr.media_aritmetica([6, 1, 4, 8]) == approx(4.75)

def test_mayores_promedio():
    assert arr.mayores_promedio([6.5, 2.1, 2.0, 2.2, 6.1]) == 2

def test_mediana_1():
    assert arr.mediana([5.0, 1.4, 3.2]) == approx(3.2)

def test_mediana_2():
    assert arr.mediana([5.0, 1.4, 3.2, 0.1]) == approx(2.3)

def test_desviacion_estandar_1():
    assert arr.desviacion_estandar([1.3, 1.3, 1.3]) == approx(0.0)

def test_desviacion_estandar_2():
    assert arr.desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0]) == approx(4.88535225615)

def test_desviacion_estandar_2():
    assert arr.desviacion_estandar([1.5, 9.5]) == approx(5.65685424949)

def test_modas_1():
    assert arr.modas([5, 4, 1, 4, 3, 3, 4, 5, 0]) == [4]

def test_modas_2():
    assert arr.modas([5, 4, 1, 4, 3, 3, 4, 5, 3]) == [3, 4]

def test_modas_3():
    assert arr.modas([5, 4, 5, 4, 3, 3, 4, 5, 3]) == [3, 4, 5]

def test_medias_moviles():
    s = [5, 2, 2, 8, -4, -1, 2]
    assert arr.medias_moviles(s, 3) == [ 3, 4, 2, 1, -1]

def test_diferencias_finitas():
    s = [5, 2, 2, 8, -4, -1, 2]
    assert arr.diferencias_finitas(s) == [ -3, 0, 6, -12, 3, 3]
