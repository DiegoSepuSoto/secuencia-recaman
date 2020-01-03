from graphics import *
from Arc import Arc


def obtiene_secuencia():
    ubicacion = 0
    linea_numeros = [False] * 10000
    secuencia = []

    for i in range(0, 2000):
        if ubicacion - i >= 0 and linea_numeros[ubicacion - i] == False:
            ubicacion -= i
        else:
            ubicacion += i
        secuencia.append(ubicacion)
        linea_numeros[ubicacion] = True
    return secuencia


secuencia = obtiene_secuencia()
win = GraphWin("Secuencia de Recaman", 1366, 768)
arriba_abajo = True
orientacion = 180

# En la recta numérica, el 0 se encuentra en la coordenada (50, 400)
x = 50
y = 768 / 2

for i in range(1, len(secuencia) - 1):
    x = 50 + secuencia[i - 1]
    salto = abs(x - (50 + secuencia[i]))
    pt_a = Point(x, y)
    pt_b = Point(50 + secuencia[i], y)
    pt1 = Point(pt_a.getX(), pt_a.getY() - salto)
    pt2 = Point(pt_b.getX(), pt_b.getY() + salto)
    if arriba_abajo:
        arc = Arc(pt1, pt2, 0, 180)
    else:
        arc = Arc(pt1, pt2, 180, 180)
    arc.draw(win)
    arriba_abajo = not arriba_abajo

win.getMouse()
win.close()
