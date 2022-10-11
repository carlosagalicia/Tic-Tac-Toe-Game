"""
Avance del proyecto python
Juego de Gato
El programa actual abre una ventana de ancho y alto definidos, despliega un menu donde el jugador puede seleccionar el
modo de juego o salir, despliega el mapa de gato dividiendo el ancho y alto de la ventana en las lineas que conforman el
area de juego uniformemente, a distancias iguales y a coordenadas definidas en la ventana. Ademas de esto, se utilizan
funciones que despliegan el menu y el mapa de gato, muestran la matriz en consola, clasifican los cuadrantes donde el
jugador hace click, evaluan si existe un ganador o se empató, y también se utilizan funciones que "juegan" contra el
jugador, colocando la figura de forma aleatoria o registrando los movimientos del jugador para determinar casos
especificos donde el jugador empate o pierda siempre dependiendo del modo de juego seleccionado.
"""
# Bibliotecas
import pygame
import random
"""
===================================================== funciones de dibujo =====================================================
"""


def menu(ventana, ancho, alto):
    """
    (uso de funciones, uso de operadores, uso de condicionales, uso de estructuras cíclicas for y while, uso de listas)
    recibe: "ventana" valor clase pygame.Surface, "ancho" valor numerico, "alto" valor numerico
    Declara el tipo de fuente a utilizar para generar texto en el menú. Genera el texto del titulo, los modos de juego y
    el boton de salida, asi como sus respectivos cuadrantes de espacio. Se despliega el menu con los elementos/opciones
    indefinidamente hasta que el usuario cierre la ventana o el mouse haga click y la posición del click esté dentro de
    una de las opciones
    devuelve: valor tipo string "exit"(salir del programa), "pvp"(jugador vs jugador),
    "pvr"(jugador vs random) o "pvc" (jugador vs computadora) dependiendo de la opcion elegida
    """
    menu = True
    font = pygame.font.SysFont("pressstart2pregular", 50)
    gato = font.render("GATO", True, (255, 255, 255), (0, 0, 0))
    gatorect = ((ancho // 2) - 90, 100)
    font = pygame.font.SysFont("pressstart2pregular", 15)
    pvp = font.render("player vs player", True, (255, 255, 255), (0, 0, 0))
    pvprect = ((ancho // 2) - 110, 220)
    pvr = font.render("player vs random", True, (255, 255, 255), (0, 0, 0))
    pvrrect = ((ancho // 2) - 105, 270)
    pvc = font.render("player vs computer", True, (255, 255, 255), (0, 0, 0))
    pvcrect = ((ancho // 2) - 120, 320)
    salir = font.render("Salir", True, (255, 255, 255), (0, 0, 0))
    salirrect = (ancho-85, 580)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                ventana.fill((0, 0, 0))
                pos = pygame.mouse.get_pos()
                if 190 < pos[0] < 430 and 220 < pos[1] < 235:
                    return "pvp"
                elif 195 < pos[0] < 435 and 270 < pos[1] < 285:
                    return "pvr"
                elif 180 < pos[0] < 450 and 320 < pos[1] < 335:
                    return "pvc"
                elif 515 < pos[0] < 590 and 580 < pos[1] < 595:
                    return "exit"
            else:
                pygame.display.flip()
                ventana.blit(gato, gatorect)
                ventana.blit(pvp, pvprect)
                ventana.blit(pvr, pvrrect)
                ventana.blit(pvc, pvcrect)
                ventana.blit(salir, salirrect)


def dibujar_gato(ventana, blanco, alto, ancho):
    """
        (uso de funciones, uso de operadores)
        recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos, "alto" valor numerico,
        "ancho" valor numerico
        Dibuja las 4 lineas blancas que integraran el area de juego de gato
        devuelve: no devuelve ningun valor
        """
    pygame.draw.line(ventana, blanco, (ancho // 3, alto), ((ancho // 3), (alto * -1)), 3)
    pygame.draw.line(ventana, blanco, ((ancho // 3)*2, alto), ((ancho // 3)*2, (alto * -1)), 3)
    pygame.draw.line(ventana, blanco, (ancho, alto // 3), (ancho * -1, alto // 3), 3)
    pygame.draw.line(ventana, blanco, (ancho, (alto // 3)*2), (ancho * -1, (alto // 3)*2), 3)


"""
================================================ funcion de despliege en consola ==============================================
"""


def imprime_matriz(gato):
    """
    (uso de funciones, uso de estructuras ciclicas for, uso de listas/matrices)
    recibe: "gato" matriz de tamaño 3x3 con valores ""/"x"/"o"
    Itera entre cada renglon o lista que contiene la matriz "gato" para imprimirla, imprimiendo toda la matriz por
    renglones
    devuelve: no devuelve ningun valor
    """
    for renglon in gato:
        print(renglon)
    print()


"""
============================================ funciones de clasificacion y logica ==============================================
"""


def machine(ventana, blanco, gato):
    """
    (uso de funciones, uso de condicionales, uso de listas/matrices)
    recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos, "gato" matriz de tamaño 3x3
    con valores ""/"x"/"o"
    En el modo de juego "pvc"(jugador vs computadora), mediante la matriz "gato" que recibe como parámetro, la función
    evalúa los cuadrantes del gato donde el usuario coloca la "x" para colocar en la matriz "gato" el circulo o la "o"
    en una "fila" y "columna" determinados como respuesta. Posteriormente se asigna un nuevo valor a la variable
    "jugada"  cada vez que se llama a esta función para guardar el caso actual y determinar nuevas filas y columnas
    donde colocar la siguiente "o" dependiendo del lugar donde el usuario coloque la siguiente "x", haciendo casi
    imposible ganar en este modo de juego. Al final de la funcion se dibuja el circulo blanco en el mapa de gato y se
    guarda el valor "o" en un espacio determinado de la matriz "gato"
    devuelve: no devuelve ningun valor
    """
    global jugada
    forma = "o"
    c_x = 0
    c_y = 0
    fila = 0
    columna = 0
    # ultimo turno
    if jugada == 6257 or jugada == 6521 or jugada == 6512:
        fila = 0
        columna = 2
    if jugada == 6152:
        fila = 2
        columna = 1
    if jugada == 8391 or jugada == 8451 or jugada == 8713 or 8931:
        fila = 0
        columna = 1
    # primer turno
    if gato[0][0] == "x" and jugada == 0:
        fila = 1
        columna = 1
        jugada = 1
    if gato[0][1] == "x" and jugada == 0:
        fila = 0
        columna = 0
        jugada = 2
    if gato[0][2] == "x" and jugada == 0:
        fila = 1
        columna = 1
        jugada = 3
    if gato[1][0] == "x" and jugada == 0:
        fila = 0
        columna = 0
        jugada = 4
    if gato[1][1] == "x" and jugada == 0:
        fila = 0
        columna = 0
        jugada = 5
    if gato[1][2] == "x" and jugada == 0:
        fila = 0
        columna = 2
        jugada = 6
    if gato[2][0] == "x" and jugada == 0:
        fila = 1
        columna = 1
        jugada = 7
    if gato[2][1] == "x" and jugada == 0:
        fila = 0
        columna = 1
        jugada = 8
    if gato[2][2] == "x" and jugada == 0:
        fila = 1
        columna = 1
        jugada = 9
    # segundo turno
    if jugada == 1:
        if gato[0][1] == "x":
            fila = 0
            columna = 2
            jugada = 12
        if gato[0][2] == "x":
            fila = 0
            columna = 1
            jugada = 13
        if gato[1][0] == "x":
            fila = 2
            columna = 0
            jugada = 14
        if gato[1][2] == "x":
            fila = 0
            columna = 1
            jugada = 16
        if gato[2][0] == "x":
            fila = 1
            columna = 0
            jugada = 17
        if gato[2][1] == "x":
            fila = 1
            columna = 0
            jugada = 18
        if gato[2][2] == "x":
            fila = 0
            columna = 1
            jugada = 19
    if jugada == 2:
        if gato[0][2] == "x":
            fila = 1
            columna = 0
            jugada = 23
        if gato[1][0] == "x":
            fila = 1
            columna = 1
            jugada = 42
        if gato[1][1] == "x":
            fila = 2
            columna = 1
            jugada = 25
        if gato[1][2] == "x":
            fila = 2
            columna = 0
            jugada = 26
        if gato[2][0] == "x":
            fila = 1
            columna = 1
            jugada = 27
        if gato[2][1] == "x":
            fila = 1
            columna = 1
            jugada = 28
        if gato[2][2] == "x":
            fila = 1
            columna = 1
            jugada = 29
    if jugada == 3:
        if gato[0][0] == "x":
            fila = 0
            columna = 1
            jugada = 13
        if gato[0][1] == "x":
            fila = 0
            columna = 0
            jugada = 32
        if gato[1][0] == "x":
            fila = 0
            columna = 0
            jugada = 43
        if gato[1][2] == "x":
            fila = 2
            columna = 2
            jugada = 36
        if gato[2][0] == "x":
            fila = 0
            columna = 1
            jugada = 37
        if gato[2][1] == "x":
            fila = 1
            columna = 0
            jugada = 38
        if gato[2][2] == "x":
            fila = 1
            columna = 2
            jugada = 39
    if jugada == 4:
        if gato[0][1] == "x":
            fila = 1
            columna = 1
            jugada = 42
        if gato[0][2] == "x":
            fila = 1
            columna = 1
            jugada = 43
        if gato[1][1] == "x":
            fila = 1
            columna = 2
            jugada = 45
        if gato[1][2] == "x":
            fila = 1
            columna = 1
            jugada = 46
        if gato[2][0] == "x":
            fila = 0
            columna = 1
            jugada = 47
        if gato[2][1] == "x":
            fila = 0
            columna = 2
            jugada = 48
        if gato[2][2] == "x":
            fila = 0
            columna = 2
            jugada = 49
    if jugada == 5:
        if gato[0][1] == "x":
            fila = 2
            columna = 1
            jugada = 25
        if gato[0][2] == "x":
            fila = 2
            columna = 0
            jugada = 53
        if gato[1][0] == "x":
            fila = 1
            columna = 2
            jugada = 45
        if gato[1][2] == "x":
            fila = 1
            columna = 0
            jugada = 56
        if gato[2][0] == "x":
            fila = 0
            columna = 2
            jugada = 57
        if gato[2][1] == "x":
            fila = 0
            columna = 1
            jugada = 58
        if gato[2][2] == "x":
            fila = 0
            columna = 2
            jugada = 59
    if jugada == 6:
        if gato[0][0] == "x":
            fila = 1
            columna = 0
            jugada = 61
        if gato[0][1] == "x":
            fila = 1
            columna = 0
            jugada = 62
        if gato[1][0] == "x":
            fila = 1
            columna = 1
            jugada = 64
        if gato[1][1] == "x":
            fila = 1
            columna = 0
            jugada = 65
        if gato[2][0] == "x":
            fila = 0
            columna = 0
            jugada = 67
        if gato[2][1] == "x":
            fila = 0
            columna = 0
            jugada = 68
        if gato[2][2] == "x":
            fila = 0
            columna = 0
            jugada = 69
    if jugada == 7:
        if gato[0][0] == "x":
            fila = 1
            columna = 0
            jugada = 17
        if gato[0][1] == "x":
            fila = 0
            columna = 0
            jugada = 27
        if gato[0][2] == "x":
            fila = 0
            columna = 1
            jugada = 37
        if gato[1][0] == "x":
            fila = 0
            columna = 0
            jugada = 74
        if gato[1][2] == "x":
            fila = 0
            columna = 1
            jugada = 76
        if gato[2][1] == "x":
            fila = 2
            columna = 2
            jugada = 78
        if gato[2][2] == "x":
            fila = 2
            columna = 1
            jugada = 79
    if jugada == 8:
        if gato[0][0] == "x":
            fila = 2
            columna = 0
            jugada = 81
        if gato[0][2] == "x":
            fila = 2
            columna = 0
            jugada = 83
        if gato[1][0] == "x":
            fila = 2
            columna = 0
            jugada = 84
        if gato[1][1] == "x":
            fila = 0
            columna = 0
            jugada = 58
        if gato[1][2] == "x":
            fila = 2
            columna = 0
            jugada = 86
        if gato[2][0] == "x":
            fila = 2
            columna = 2
            jugada = 87
        if gato[2][2] == "x":
            fila = 2
            columna = 0
            jugada = 89
    if jugada == 9:
        if gato[0][0] == "x":
            fila = 0
            columna = 1
            jugada = 19
        if gato[0][1] == "x":
            fila = 0
            columna = 0
            jugada = 29
        if gato[0][2] == "x":
            fila = 1
            columna = 2
            jugada = 39
        if gato[1][0] == "x":
            fila = 0
            columna = 0
            jugada = 94
        if gato[1][2] == "x":
            fila = 0
            columna = 2
            jugada = 96
        if gato[2][0] == "x":
            fila = 2
            columna = 1
            jugada = 79
        if gato[2][1] == "x":
            fila = 2
            columna = 0
            jugada = 98

    # tercer turno
    if jugada == 12:
        if gato[1][0] == "x" or gato[1][2] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 1
            columna = 0
            jugada = 127
    if jugada == 13:
        if gato[1][0] == "x" or gato[1][2] == "x" or gato[2][0] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 1
            columna = 0
            jugada = 138
    if jugada == 14:
        if gato[0][1] == "x" or gato[1][2] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 0
            columna = 1
            jugada = 143
    if jugada == 16:
        if gato[0][2] == "x" or gato[1][0] == "x" or gato[2][0] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 1
        if gato[2][1]:
            fila = 2
            columna = 0
            jugada = 168
    if jugada == 17:
        if gato[0][1] == "x" or gato[0][2] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 0
            columna = 1
            jugada = 176
    if jugada == 18:
        if gato[0][1] == "x" or gato[0][2] == "x" or gato[2][0] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 0
            columna = 2
            jugada = 186
    if jugada == 19:
        if gato[0][2] == "x" or gato[1][0] == "x" or gato[1][2] == "x" or gato[2][0]:
            fila = 2
            columna = 1
        if gato[2][1]:
            fila = 2
            columna = 0
            jugada = 198
    if jugada == 23:
        if gato[1][1] == "x" or gato[1][2] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0]:
            fila = 1
            columna = 1
            jugada = 237
    if jugada == 25:
        if gato[0][2] == "x":
            fila = 2
            columna = 0
            jugada = 253
        if gato[1][0] == "x":
            fila = 1
            columna = 2
            jugada = 452
        if gato[1][2] == "x":
            fila = 1
            columna = 0
            jugada = 256
        if gato[2][0] == "x":
            fila = 0
            columna = 2
            jugada = 257
        if gato[2][2] == "x":
            fila = 0
            columna = 2
            jugada = 259
    if jugada == 26:
        if gato[0][2] == "x" or gato[1][1] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 1
            columna = 1
            jugada = 264
    if jugada == 27:
        if gato[0][2] == "x" or gato[1][0] == "x" or gato[1][2] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2]:
            fila = 2
            columna = 1
            jugada = 279
    if jugada == 28:
        if gato[0][2] == "x" or gato[1][0] == "x" or gato[1][2] == "x" or gato[2][0] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 2
            columna = 0
            jugada = 289
    if jugada == 29:
        if gato[0][2] == "x":
            fila = 1
            columna = 2
            jugada = 293
        if gato[1][0] == "x":
            fila = 0
            columna = 2
            jugada = 429
        if gato[1][2] == "x":
            fila = 0
            columna = 2
            jugada = 296
        if gato[2][0] == "x":
            fila = 2
            columna = 1
            jugada = 297
        if gato[2][1] == "x":
            fila = 2
            columna = 0
            jugada = 298
    if jugada == 32:
        if gato[1][0] == "x" or gato[1][2] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 1
            columna = 2
            jugada = 329
    if jugada == 36:
        if gato[0][1] == "x" or gato[1][0] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 0
            columna = 1
            jugada = 361
    if jugada == 37:
        if gato[0][0] == "x" or gato[1][0] == "x" or gato[1][2] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 2
            columna = 2
            jugada = 378
    if jugada == 38:
        if gato[0][0] == "x" or gato[0][1] == "x" or gato[2][0] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 2
            columna = 2
            jugada = 386
    if jugada == 39:
        if gato[0][0] == "x" or gato[0][1] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 0
            columna = 0
            jugada = 394
    if jugada == 42:
        if gato[0][2] == "x" or gato[1][2] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 0
            columna = 2
            jugada = 429
    if jugada == 43:
        if gato[0][1] == "x" or gato[1][2] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 1
            columna = 2
            jugada = 439
    if jugada == 45:
        if gato[0][1] == "x":
            fila = 2
            columna = 1
            jugada = 452
        if gato[0][2] == "x":
            fila = 2
            columna = 0
            jugada = 453
        if gato[2][0] == "x":
            fila = 0
            columna = 2
            jugada = 457
        if gato[2][1] == "x":
            fila = 0
            columna = 1
            jugada = 458
        if gato[2][2] == "x":
            fila = 0
            columna = 1
            jugada = 459
    if jugada == 46:
        if gato[0][1] == "x" or gato[0][2] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 0
            columna = 2
            jugada = 469
    if jugada == 47:
        if gato[1][1] == "x" or gato[1][2] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 1
            jugada = 473
    if jugada == 48:
        if gato[1][1] == "x" or gato[1][2] == "x" or gato[2][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 1
            columna = 1
            jugada = 482
    if jugada == 49:
        if gato[1][1] == "x" or gato[1][2] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 1
            columna = 1
            jugada = 429
    if jugada == 53:
        if gato[0][1] == "x" or gato[1][2] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 1
            columna = 2
            jugada = 453
    if jugada == 56:
        if gato[0][1] == "x" or gato[0][2] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 0
            columna = 2
            jugada = 567
    if jugada == 57:
        if gato[1][0] == "x" or gato[1][2] == "x" or gato[2][1] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 2
            columna = 1
            jugada = 257
    if jugada == 58:
        if gato[1][0] == "x" or gato[1][2] == "x" or gato[2][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 0
            jugada = 583
    if jugada == 59:
        if gato[1][0] == "x" or gato[1][2] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 2
            columna = 1
            jugada = 592
    if jugada == 61:
        if gato[0][1] == "x":
            fila = 1
            columna = 1
            jugada = 612
        if gato[1][1] == "x":
            fila = 2
            columna = 2
            jugada = 615
        if gato[2][0] == "x":
            fila = 1
            columna = 1
            jugada = 617
        if gato[2][1] == "x":
            fila = 1
            columna = 1
            jugada = 618
        if gato[2][2] == "x":
            fila = 1
            columna = 1
            jugada = 619
    if jugada == 62:
        if gato[0][0] == "x":
            fila = 1
            columna = 1
            jugada = 621
        if gato[1][1] == "x":
            fila = 2
            columna = 1
            jugada = 625
        if gato[2][0] == "x":
            fila = 1
            columna = 1
            jugada = 627
        if gato[2][1] == "x":
            fila = 1
            columna = 1
            jugada = 628
        if gato[2][2] == "x":
            fila = 2
            columna = 0
            jugada = 629
    if jugada == 64:
        if gato[0][0] == "x" or gato[0][1] == "x" or gato[2][2] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 0
            columna = 0
            jugada = 647
    if jugada == 65:
        if gato[0][0] == "x":
            fila = 2
            columna = 2
            jugada = 651
        if gato[0][1] == "x":
            fila = 2
            columna = 1
            jugada = 652
        if gato[2][0] == "x":
            fila = 0
            columna = 0
            jugada = 657
        if gato[2][1] == "x":
            fila = 0
            columna = 1
            jugada = 658
        if gato[2][2] == "x":
            fila = 0
            columna = 0
            jugada = 659
    if jugada == 67:
        if gato[2][2] == "x" or gato[2][1] == "x" or gato[1][0] == "x" or gato[1][1] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 1
            columna = 1
            jugada = 672
    if jugada == 68:
        if gato[2][2] == "x" or gato[2][0] == "x" or gato[1][0] == "x" or gato[1][1] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 1
            columna = 1
            jugada = 682
    if jugada == 69:
        if gato[1][0] == "x" or gato[1][1] == "x" or gato[2][0] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 2
            columna = 0
            jugada = 692
    if jugada == 74:
        if gato[0][1] == "x" or gato[0][2] == "x" or gato[1][2] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 2
            columna = 1
            jugada = 749
    if jugada == 76:
        if gato[0][0] == "x" or gato[0][2] == "x" or gato[1][0] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 2
            columna = 2
            jugada = 768
    if jugada == 78:
        if gato[0][1] == "x" or gato[0][2] == "x" or gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 0
            jugada = 781
    if jugada == 79:
        if gato[0][0] == "x" or gato[0][2] == "x" or gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 0
            columna = 0
            jugada = 792
    if jugada == 81:
        if gato[0][2] == "x":
            fila = 1
            columna = 1
            jugada = 813
        if gato[1][0] == "x":
            fila = 1
            columna = 1
            jugada = 814
        if gato[1][1] == "x":
            fila = 2
            columna = 2
            jugada = 815
        if gato[1][2] == "x":
            fila = 1
            columna = 1
            jugada = 816
        if gato[2][2] == "x":
            fila = 1
            columna = 1
            jugada = 819
    if jugada == 83:
        if gato[0][0] == "x":
            fila = 1
            columna = 1
            jugada = 831
        if gato[1][0] == "x":
            fila = 1
            columna = 1
            jugada = 834
        if gato[1][1] == "x":
            fila = 0
            columna = 0
            jugada = 835
        if gato[1][2] == "x":
            fila = 2
            columna = 2
            jugada = 836
        if gato[2][2] == "x":
            fila = 1
            columna = 2
            jugada = 839
    if jugada == 84:
        if gato[0][0] == "x":
            fila = 1
            columna = 1
            jugada = 841
        if gato[0][2] == "x":
            fila = 1
            columna = 1
            jugada = 843
        if gato[1][1] == "x":
            fila = 1
            columna = 2
            jugada = 845
        if gato[1][2] == "x":
            fila = 1
            columna = 1
            jugada = 846
        if gato[2][2] == "x":
            fila = 0
            columna = 2
            jugada = 849
    if jugada == 86:
        if gato[0][0] == "x":
            fila = 1
            columna = 1
            jugada = 861
        if gato[0][2] == "x":
            fila = 2
            columna = 2
            jugada = 863
        if gato[1][0] == "x":
            fila = 1
            columna = 1
            jugada = 864
        if gato[1][1] == "x":
            fila = 1
            columna = 0
            jugada = 865
        if gato[2][2] == "x":
            fila = 0
            columna = 2
            jugada = 869
    if jugada == 87:
        if gato[0][0] == "x":
            fila = 1
            columna = 0
            jugada = 871
        if gato[0][2] == "x":
            fila = 1
            columna = 1
            jugada = 873
        if gato[1][0] == "x":
            fila = 0
            columna = 0
            jugada = 874
        if gato[1][1] == "x":
            fila = 0
            columna = 2
            jugada = 875
        if gato[1][2] == "x":
            fila = 0
            columna = 0
            jugada = 876
    if jugada == 89:
        if gato[0][0] == "x":
            fila = 1
            columna = 1
            jugada = 891
        if gato[0][2] == "x":
            fila = 1
            columna = 2
            jugada = 893
        if gato[1][0] == "x":
            fila = 0
            columna = 2
            jugada = 894
        if gato[1][1] == "x":
            fila = 0
            columna = 0
            jugada = 895
        if gato[1][2] == "x":
            fila = 0
            columna = 2
            jugada = 896
    if jugada == 94:
        if gato[0][1] == "x":
            fila = 0
            columna = 2
            jugada = 942
        if gato[0][2] == "x":
            fila = 1
            columna = 2
            jugada = 943
        if gato[1][2] == "x":
            fila = 0
            columna = 2
            jugada = 946
        if gato[2][0] == "x":
            fila = 2
            columna = 1
            jugada = 947
        if gato[2][1] == "x":
            fila = 2
            columna = 0
            jugada = 948
    if jugada == 96:
        if gato[0][1] == "x" or gato[0][0] == "x" or gato[1][0] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
            jugada = 967
    if jugada == 98:
        if gato[0][0] == "x" or gato[0][1] == "x" or gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 2
            jugada = 983

    # cuarto turno
    if jugada == 127:
        if gato[2][1] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2]:
            fila = 2
            columna = 1
    if jugada == 138:
        if gato[2][0] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 2
            columna = 2
    if jugada == 143:
        if gato[1][2] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 1
            columna = 2
    if jugada == 168:
        if gato[1][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 2
    if jugada == 176:
        if gato[0][2] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 1
        if gato[2][1]:
            fila = 2
            columna = 2
    if jugada == 186:
        if gato[0][1] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 2
    if jugada == 198:
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 2
    if jugada == 237:
        if gato[2][1] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 2
            columna = 2
    if jugada == 253:
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 1
            columna = 0
    if jugada == 256:
        if gato[0][2] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 0
            columna = 2
    if jugada == 257:
        if gato[1][0] == "x":
            fila = 1
            columna = 2
            jugada = 2574
        if gato[1][2] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 0
    if jugada == 259:
        if gato[1][0] == "x":
            fila = 1
            columna = 2
            jugada = 2594
        if gato[1][2] == "x" or gato[2][0] == "x":
            fila = 1
            columna = 0
    if jugada == 264:
        if gato[2][1] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 2
    if jugada == 279:
        if gato[0][2] == "x":
            fila = 1
            columna = 2
            jugada = 2793
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
    if jugada == 289:
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 0
    if jugada == 293:
        if gato[2][0] == "x" or gato[2][1] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 2
            columna = 0
    if jugada == 296:
        if gato[1][0] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
    if jugada == 297:
        if gato[0][2] == "x":
            fila = 1
            columna = 2
            jugada = 2973
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
    if jugada == 298:
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 0
    if jugada == 329:
        if gato[2][1] == "x" or gato[2][0] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 2
            columna = 0
    if jugada == 361:
        if gato[1][0] == "x" or gato[2][0] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 1
            columna = 0
    if jugada == 378:
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 0
    if jugada == 386:
        if gato[0][1] == "x" or gato[2][0] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 0
            columna = 1
    if jugada == 394:
        if gato[0][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 2
            columna = 0
    if jugada == 429:
        if gato[1][2] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
    if jugada == 439:
        if gato[0][1] == "x":
            fila = 2
            columna = 0
        if gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
    if jugada == 452:
        if gato[0][2] == "x":
            fila = 2
            columna = 0
            jugada = 4523
        if gato[2][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
    if jugada == 453:
        if gato[0][1] == "x":
            fila = 2
            columna = 1
            jugada = 4532
        if gato[2][1] == "x":
            fila = 0
            columna = 1
        if gato[2][2] == "x":
            fila = 0
            columna = 1
    if jugada == 457:
        if gato[0][1] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 0
            columna = 1
    if jugada == 458:
        if gato[2][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 0
    if jugada == 459:
        if gato[2][0] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 0
    if jugada == 469:
        if gato[0][1] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 0
            columna = 1
    if jugada == 473:
        if gato[1][2] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 2
            columna = 2
    if jugada == 482:
        if gato[1][2] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 2
    if jugada == 567:
        if gato[2][1] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 2
            columna = 1
    if jugada == 583:
        if gato[1][2] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 1
            columna = 2
    if jugada == 592:
        if gato[1][0] == "x":
            fila = 1
            columna = 2
            jugada = 5924
        if gato[1][2] == "x":
            fila = 1
            columna = 0
        if gato[2][0] == "x":
            fila = 1
            columna = 0
    if jugada == 612:
        if gato[2][1] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
    if jugada == 615:
        if gato[0][1] == "x":
            fila = 2
            columna = 1
            jugada = 6152
        if gato[2][0] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 1
    if jugada == 617:
        if gato[0][1] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 2
            columna = 1
    if jugada == 618:
        if gato[0][1] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 2
    if jugada == 619:
        if gato[0][1] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
    if jugada == 621:
        if gato[2][1] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
    if jugada == 625:
        if gato[0][0] == "x":
            fila = 2
            columna = 2
            jugada = 6257
        if gato[2][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 0
    if jugada == 627:
        if gato[0][0] == "x":
            fila = 2
            columna = 1
        if gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 2
            columna = 1
    if jugada == 628:
        if gato[0][0] == "x" or gato[2][2] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 2
    if jugada == 629:
        if gato[1][1] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 1
    if jugada == 647:
        if gato[0][1] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 0
            columna = 1
    if jugada == 651:
        if gato[0][1] == "x":
            fila = 2
            columna = 1
            jugada = 6512
        if gato[2][0] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 1
    if jugada == 652:
        if gato[0][0] == "x":
            fila = 2
            columna = 2
            jugada = 6521
        if gato[2][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 0
    if jugada == 657:
        if gato[2][2] == "x" or gato[2][1] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 2
            columna = 1
    if jugada == 658:
        if gato[2][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 2
            columna = 2
    if jugada == 659:
        if gato[2][1] == "x" or gato[2][0] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 2
            columna = 0
    if jugada == 672:
        if gato[1][0] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 2
            columna = 1
    if jugada == 682:
        if gato[1][0] == "x" or gato[2][0] == "x":
            fila = 2
            columna = 2
        if gato[2][2] == "x":
            fila = 2
            columna = 0
    if jugada == 692:
        if gato[1][1] == "x" or gato[2][1] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 1
            columna = 1
    if jugada == 749:
        if gato[0][2] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 0
            columna = 2
    if jugada == 768:
        if gato[0][2] == "x" or gato[1][0] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 0
    if jugada == 781:
        if gato[0][1] == "x" or gato[0][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 0
            columna = 1
    if jugada == 792:
        if gato[0][2] == "x":
            fila = 1
            columna = 2
            jugada = 7923
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
    if jugada == 813:
        if gato[1][0] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 2
            columna = 2
    if jugada == 814:
        if gato[2][2] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 2
    if jugada == 815:
        if gato[0][2] == "x" or gato[1][2] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 1
            columna = 2
    if jugada == 816:
        if gato[1][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 2
    if jugada == 819:
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 2
    if jugada == 831:
        if gato[1][0] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 2
            columna = 2
    if jugada == 834:
        if gato[0][0] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 2
            columna = 2
    if jugada == 835:
        if gato[1][2] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 1
            columna = 2
    if jugada == 836:
        if gato[0][0] == "x" or gato[1][1] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 1
            columna = 1
    if jugada == 839:
        if gato[0][0] == "x":
            fila = 1
            columna = 1
            jugada = 8391
        if gato[1][0] == "x" or gato[1][1] == "x":
            fila = 0
            columna = 0
    if jugada == 841:
        if gato[1][2] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 2
    if jugada == 843:
        if gato[0][0] == "x" or gato[2][2] == "x":
            fila = 1
            columna = 2
        if gato[1][2] == "x":
            fila = 2
            columna = 2
    if jugada == 845:
        if gato[0][0] == "x":
            fila = 2
            columna = 2
            jugada = 8451
        if gato[0][2] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 0
    if jugada == 846:
        if gato[0][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 2
    if jugada == 849:
        if gato[1][1] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 1
    if jugada == 861:
        if gato[1][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 2
    if jugada == 863:
        if gato[0][0] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 1
            columna = 1
        if gato[1][1] == "x":
            fila = 1
            columna = 0
    if jugada == 864:
        if gato[0][0] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 2
            columna = 2
    if jugada == 865:
        if gato[0][2] == "x" or gato[2][2] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 2
            columna = 2
    if jugada == 869:
        if gato[1][0] == "x" or gato[1][1] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 1
    if jugada == 871:
        if gato[0][2] == "x":
            fila = 1
            columna = 1
            jugada = 8713
        if gato[1][1] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
    if jugada == 873:
        if gato[1][0] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 0
    if jugada == 874:
        if gato[1][2] == "x" or gato[1][1] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 1
    if jugada == 875:
        if gato[1][2] == "x" or gato[1][0] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 2
    if jugada == 876:
        if gato[1][0] == "x" or gato[1][1] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 1
    if jugada == 891:
        if gato[1][2] == "x" or gato[1][0] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 2
    if jugada == 893:
        if gato[0][0] == "x":
            fila = 1
            columna = 1
            jugada = 8931
        if gato[1][0] == "x" or gato[1][1] == "x":
            fila = 0
            columna = 0
    if jugada == 894:
        if gato[1][1] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 1
    if jugada == 895:
        if gato[1][2] == "x" or gato[1][0] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 0
    if jugada == 896:
        if gato[1][0] == "x" or gato[1][1] == "x":
            fila = 0
            columna = 0
        if gato[0][0] == "x":
            fila = 1
            columna = 1
    if jugada == 942:
        if gato[1][2] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
    if jugada == 943:
        if gato[0][1] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 2
            columna = 1
    if jugada == 946:
        if gato[0][1] == "x" or gato[2][1] == "x":
            fila = 2
            columna = 0
        if gato[2][0] == "x":
            fila = 0
            columna = 1
    if jugada == 947:
        if gato[0][2] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 0
            columna = 2
    if jugada == 948:
        if gato[0][1] == "x" or gato[1][2] == "x":
            fila = 0
            columna = 2
        if gato[0][2] == "x":
            fila = 1
            columna = 2
    if jugada == 967:
        if gato[0][0] == "x" or gato[1][0] == "x":
            fila = 0
            columna = 1
        if gato[0][1] == "x":
            fila = 0
            columna = 0
    if jugada == 983:
        if gato[0][0] == "x" or gato[0][1] == "x":
            fila = 1
            columna = 0
        if gato[1][0] == "x":
            fila = 0
            columna = 0
    if fila == 0 and columna == 0:
        c_x = 100
        c_y = 100

    elif fila == 0 and columna == 1:
        c_x = 300
        c_y = 100

    elif fila == 0 and columna == 2:
        c_x = 500
        c_y = 100

    elif fila == 1 and columna == 0:
        c_x = 100
        c_y = 300

    elif fila == 1 and columna == 1:
        c_x = 300
        c_y = 300

    elif fila == 1 and columna == 2:
        c_x = 500
        c_y = 300

    elif fila == 2 and columna == 0:
        c_x = 100
        c_y = 500

    elif fila == 2 and columna == 1:
        c_x = 300
        c_y = 500

    elif fila == 2 and columna == 2:
        c_x = 500
        c_y = 500
    pygame.draw.circle(ventana, blanco, (c_x, c_y), 80, 3)
    gato[fila][columna] = "o"


def random_machine(ventana, blanco, gato):
    """
    (uso de funciones, uso de operadores, uso de condicionales, uso de estructuras ciclicas for/while, uso de
    listas/matrices)
    recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos, "gato" matriz de tamaño 3x3
    con valores ""/"x"/"o"
    En el modo de juego "pvr" (jugador vs random", escoge al azar una "fila" y "columna" para colocar la "o".
    Si todos los elementos de la matriz "gato" contienen una "x" o una "o" no realiza ninguna accion y retorna
    verdadero debido a que el gato ya se encuentra lleno. Ademas, itera cambiando los valores de las columnas y filas
    hasta que encuentre un espacio en la matriz vacio para posteriormente colocar la "o" en la matriz y en el mapa de
    gato con un circulo blanco
    devuelve: no devuelve ningun valor
    """
    forma = "o"
    c_x = 0
    c_y = 0
    fila = random.randint(0, 2)
    columna = random.randint(0, 2)

    llenos = 0
    for renglon in gato:
        for ele in renglon:
            if ele != "":
                llenos += 1
            if llenos == 9:
                return 1
    while gato[fila][columna] != "":
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)

    if fila == 0 and columna == 0:
        c_x = 100
        c_y = 100

    elif fila == 0 and columna == 1:
        c_x = 300
        c_y = 100

    elif fila == 0 and columna == 2:
        c_x = 500
        c_y = 100

    elif fila == 1 and columna == 0:
        c_x = 100
        c_y = 300

    elif fila == 1 and columna == 1:
        c_x = 300
        c_y = 300

    elif fila == 1 and columna == 2:
        c_x = 500
        c_y = 300

    elif fila == 2 and columna == 0:
        c_x = 100
        c_y = 500

    elif fila == 2 and columna == 1:
        c_x = 300
        c_y = 500

    elif fila == 2 and columna == 2:
        c_x = 500
        c_y = 500
    pygame.draw.circle(ventana, blanco, (c_x, c_y), 80, 3)
    gato[fila][columna] = "o"


def clasificar_x(ventana, blanco, gato, juego):
    """
    (uso de funciones, uso de operadores, uso de condicionales, uso de listas/matrices)
    recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos, "gato" matriz de tamaño 3x3 con
    valores ""/"x"/"o", "juego" variable tipo string con valores "pvr" o "pvc" dependiendo del modo de juego elegido
    La funcion registra la posicion actual en "x" y "y" del mouse cuando hizo click y determina una fila y columna
    donde se coloca la "x" en la matriz "gato" y en el mapa de gato dependiendo del cuadrante donde se hizo click.
    Además, se llama a las funciones de respuesta dependiendo del modo de juego "pvr"(jugador vs random) o
    "pvc" (jugador vs computadora). Lo anterior se lleva a cabo siempre y cuando el usuario haga click en un cuadrante
    vacio
    devuelve: no devuelve ningun valor
    """
    c_x = 0
    c_y = 0
    fila = 0
    columna = 0
    pos = pygame.mouse.get_pos()
    if 0 <= pos[1] < 200:
        c_y = 100
        if 0 <= pos[0] < 200:
            c_x = 100
            fila = 0
            columna = 0

        elif 200 <= pos[0] < 400:
            c_x = 300
            fila = 0
            columna = 1

        elif 400 <= pos[0] <= 600:
            c_x = 500
            fila = 0
            columna = 2

    elif 200 <= pos[1] < 400:
        c_y = 300
        if 0 <= pos[0] < 200:
            c_x = 100
            fila = 1
            columna = 0

        elif 200 <= pos[0] < 400:
            c_x = 300
            fila = 1
            columna = 1

        elif 400 <= pos[0] <= 600:
            c_x = 500
            fila = 1
            columna = 2

    elif 400 <= pos[1] <= 600:
        c_y = 500
        if 0 <= pos[0] < 200:
            c_x = 100
            fila = 2
            columna = 0

        elif 200 <= pos[0] < 400:
            c_x = 300
            fila = 2
            columna = 1

        elif 400 <= pos[0] <= 600:
            c_x = 500
            fila = 2
            columna = 2

    if gato[fila][columna] == "":
        gato[fila][columna] = "x"
        pygame.draw.line(ventana, blanco, (c_x + 80, c_y + 80), (c_x - 80, c_y - 80), 3)
        pygame.draw.line(ventana, blanco, (c_x + 80, c_y - 80), (c_x - 80, c_y + 80), 3)
        if juego == "pvr":
            random_machine(ventana, blanco, gato)
        if juego == "pvc":
            machine(ventana, blanco, gato)
    imprime_matriz(gato)


def clasificar(ventana, blanco, gato):
    """
    (uso de funciones, uso de operadores, uso de condicionales, uso de listas\matrices)
    recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos, "gato" matriz de tamaño 3x3
    con valores ""/"x"/"o"
    En el modo de juego "pvp" (jugador vs jugador), la funcion determina la posicion x,y del mouse y asigna el lugar en
    la matriz y en el mapa donde la figura "x"/"o" se coloca dependiendo del cuadrante donde los jugadores hacen click.
    Además, se cambia la figura a colocar con cada turno de "x" a "o" y viceversa. Lo anterior se lleva a cabo siempre
    y cuando los usuarios haga click en un cuadrante vacio
    devuelve: no devuelve ningun valor
    """
    global forma
    forma_colocada = ""
    c_x = 0
    c_y = 0
    fila = 0
    columna = 0
    pos = pygame.mouse.get_pos()
    if 0 <= pos[1] < 200:
        c_y = 100
        if 0 <= pos[0] < 200:
            c_x = 100
            fila = 0
            columna = 0

        elif 200 <= pos[0] < 400:
            c_x = 300
            fila = 0
            columna = 1

        elif 400 <= pos[0] <= 600:
            c_x = 500
            fila = 0
            columna = 2

    elif 200 <= pos[1] < 400:
        c_y = 300
        if 0 <= pos[0] < 200:
            c_x = 100
            fila = 1
            columna = 0

        elif 200 <= pos[0] < 400:
            c_x = 300
            fila = 1
            columna = 1

        elif 400 <= pos[0] <= 600:
            c_x = 500
            fila = 1
            columna = 2

    elif 400 <= pos[1] <= 600:
        c_y = 500
        if 0 <= pos[0] < 200:
            c_x = 100
            fila = 2
            columna = 0

        elif 200 <= pos[0] < 400:
            c_x = 300
            fila = 2
            columna = 1

        elif 400 <= pos[0] <= 600:
            c_x = 500
            fila = 2
            columna = 2

    if gato[fila][columna] == "":
        gato[fila][columna] = forma
        if forma == "x":
            pygame.draw.line(ventana, blanco, (c_x + 80, c_y + 80), (c_x - 80, c_y - 80), 3)
            pygame.draw.line(ventana, blanco, (c_x + 80, c_y - 80), (c_x - 80, c_y + 80), 3)
            forma_colocada = "x"
            forma = "o"
        else:
            pygame.draw.circle(ventana, blanco, (c_x, c_y), 80, 3)
            forma_colocada = "o"
            forma = "x"
    imprime_matriz(gato)


"""
========================================== funcion de evaluacion de resultados ===============================================
"""


def evaluar(gato):
    """
    (uso de funciones, uso de estructuras condicionales, uso de listas/matrices)
    recibe: "gato" matriz de tamaño 3x3 con valores ""/"x"/"o"
    Determina si se repite la forma "x" u "o" tres veces horizontal, vertical o diagonalmente retornando el caracter "x"
    u "o". En el caso de que ninguna se repita retorna ""
    devuelve: "forma" variable tipo matriz con valor "x", "o" o ""
    """
    forma = ""
    if gato[0][0] == gato[0][1] == gato[0][2] and gato[0][0] == "x":
        return gato[0][0]
    elif gato[1][0] == gato[1][1] == gato[1][2] and gato[1][0] == "x":
        return gato[1][0]
    elif gato[2][0] == gato[2][1] == gato[2][2] and gato[2][0] == "x":
        return gato[2][0]
    elif gato[0][0] == gato[1][0] == gato[2][0] and gato[0][0] == "x":
        return gato[0][0]
    elif gato[0][1] == gato[1][1] == gato[2][1] and gato[0][1] == "x":
        return gato[0][1]
    elif gato[0][2] == gato[1][2] == gato[2][2] and gato[0][2] == "x":
        return gato[0][2]
    elif gato[0][0] == gato[1][1] == gato[2][2] and gato[0][0] == "x":
        return gato[0][0]
    elif gato[0][2] == gato[1][1] == gato[2][0] and gato[0][2] == "x":
        return gato[0][2]
    elif gato[0][0] == gato[0][1] == gato[0][2] and gato[0][0] == "o":
        return gato[0][0]
    elif gato[1][0] == gato[1][1] == gato[1][2] and gato[1][0] == "o":
        return gato[1][0]
    elif gato[2][0] == gato[2][1] == gato[2][2] and gato[2][0] == "o":
        return gato[2][0]
    elif gato[0][0] == gato[1][0] == gato[2][0] and gato[0][0] == "o":
        return gato[0][0]
    elif gato[0][1] == gato[1][1] == gato[2][1] and gato[0][1] == "o":
        return gato[0][1]
    elif gato[0][2] == gato[1][2] == gato[2][2] and gato[0][2] == "o":
        return gato[0][2]
    elif gato[0][0] == gato[1][1] == gato[2][2] and gato[0][0] == "o":
        return gato[0][0]
    elif gato[0][2] == gato[1][1] == gato[2][0] and gato[0][2] == "o":
        return gato[0][2]
    return forma


"""
============================================= funcion de despliegue de botones  ==============================================
"""


def boton_salir_o_jugar(ventana, ancho, text):
    """
    (uso de funciones, uso de operadores, uso de condicionales, uso de estructuras ciclicas for y while, uso de listas)
    recibe: "ventana" valor clase pygame.Surface, "ancho" valor numerico, "text" valor tipo string
    Funcion llamada al final de las partidas. Declara el tipo de fuente a utilizar para generar texto. Genera el texto
    de las opciones de salida y de reinicio de partida, así como del ganador o empate mediante la variable "text"
    indefinidamente hasta que el usuario cierre la ventana o el mouse haga click y la posición del click esté dentro de
    los rectangulos delimitadores de una de las opciones
    devuelve: valor tipo string "restart" o "volver"
    """
    font = pygame.font.SysFont("pressstart2pregular", 15)
    pygame.draw.rect(ventana, (0, 0, 0), (100, 450, 400, 100))
    texto = font.render(text, True, (255, 255, 255), (0, 0, 0))
    texto_rect = (ancho - 400, 460)
    bot_salir = font.render("Salir", True, (255, 255, 255), (0, 0, 0))
    bot_salir_rect = (ancho - 210, 495)
    bot_jugar = font.render("Jugar de nuevo", True, (255, 255, 255), (0, 0, 0))
    bot_jugar_rect = (ancho - 460, 495)
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 140 < pos[0] < 350 and 495 < pos[1] < 510:
                    return "restart"
                elif 390 < pos[0] < 465 and 495 < pos[1] < 510:
                    return "volver"

            else:
                pygame.display.flip()
                ventana.blit(bot_salir, bot_salir_rect)
                ventana.blit(bot_jugar, bot_jugar_rect)
                ventana.blit(texto, texto_rect)


"""
============================================= funciones de prueba  ==============================================
================================== funciones que reciben matrices como parámetros ===============================
"""


def prueba():
    # entrada matriz gato = [["x", "o", "o"], ["x", "o", "x"], ["x", "o", ""]]
    # salida string "x"
    gato = [["x", "o", "o"], ["x", "o", "x"], ["x", "o", ""]]
    print(evaluar(gato))
    # entrada matriz gato = [["x", "o", "o"], ["x", "o", "x"], ["x", "o", ""]]
    # salida matriz
    # ['x', 'o', 'o']
    # ['x', 'o', 'x']
    # ['x', 'o', '']
    imprime_matriz(gato)


"""
============================================= funcion principal main  ==============================================
"""


def main():
    """
    (uso de funciones, uso de operadores, uso de condicionales, uso de estructuras ciclicas for/while, uso de listas/matrices)
    recibe: ningun valor
    Crea la matriz "gato" donde se colocaran los valores "x" y "o", despliega la ventana de juego, llama a la funcion
    que despliega el menu y almacena el valor de tipo de juego u opcion seleccionado en la variable "juego", dibuja el
    mapa de juego si el usuario no selecciona la opcion de salir y utiliza estructuras while y for para leer cada evento.
    Si el tipo de evento es un click y el/los usuarios se encuentran en una partida llama a las funciones dependiendo
    del valor de la variable "juego" y evalua si existe un ganador. Si hay un ganador la variable "texto" guarda quien
    ganó o, si se llenan todos los cuadrantes y no hay ganador, la variable "texto" adquiere el valor tipo string de
    "Empate!" y pasa como parametro a la funcion que despliega los botones al final de cada partida y guarda el valor
    tipo string que retorna en la variable "boton".
    Si el usuario hace click en el boton "volver", la variable "boton" adquiere el valor tipo string "volver", llenando la
    ventana de negro, desplegando el menu, reiniciando la matriz "gato" y los valores en caso de que el jugador decida
    jugar de nuevo y seleccione otro modo de juego.
    Si el usuario hace click en el boton "jugar de nuevo", la variable "boton" adquiere el valor tipo string "restart",
    llenando la ventana de negro, reiniciando la matriz "gato" y los valores pero no reinicia el modo de juego para que
    el jugador pueda jugar de nuevo en el mismo modo de juego.
    Si se detecta un evento de salida (como cerrar la ventana o presionar el boton "salir" del menu) el ciclo while que
    antes era verdadero y actualizaba la ventana se convierte en falso y termina el programa.
    devuelve: no devuelve ningun valor
    """
    global jugada
    global forma
    gato = [["", "", ""], ["", "", ""], ["", "", ""]]
    ancho = 600
    alto = 600
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    boton = ""
    estado = True
    partida = True
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    juego = menu(ventana, ancho, alto)
    if juego == "exit":
        estado = False
    else:
        dibujar_gato(ventana, blanco, alto, ancho)

    while estado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or juego == "exit":
                estado = False
            elif event.type == pygame.MOUSEBUTTONDOWN and partida is True:
                if juego == "pvp":
                    clasificar(ventana, blanco, gato)
                elif juego == "pvr" or "pvc":
                    clasificar_x(ventana, blanco, gato, juego)
                ganador = evaluar(gato)
                if ganador != "":
                    text = "¡El ganador es " + str(ganador) + "!"
                    boton = boton_salir_o_jugar(ventana, ancho, text)
                    partida = False
                llenos = 0
                for renglon in gato:
                    for ele in renglon:
                        if ele != "":
                            llenos += 1
                        if llenos == 9 and ganador == "":
                            text = "¡Empate!"
                            boton = boton_salir_o_jugar(ventana, ancho, text)
                            partida = False
                if boton == "volver":
                    ventana.fill((0, 0, 0))
                    juego = menu(ventana, ancho, alto)
                    dibujar_gato(ventana, blanco, alto, ancho)
                    boton = ""
                    gato = [["", "", ""], ["", "", ""], ["", "", ""]]
                    partida = True
                    jugada = 0
                    forma = "x"
                    text = 0
                    continue
                if boton == "restart":
                    ventana.fill((0, 0, 0))
                    dibujar_gato(ventana, blanco, alto, ancho)
                    boton = ""
                    gato = [["", "", ""], ["", "", ""], ["", "", ""]]
                    partida = True
                    jugada = 0
                    forma = "x"
                    text = 0
                    continue
                if juego == "exit":
                    estado = False
        pygame.display.flip()
    pygame.quit()


"""
================================ parte principal del programa =======================================
"""
jugada = 0
forma = "x"
main()
# la función prueba ejecuta las 2 funciones que pueden recibir parametros y retornar datos tipo string u otras matrices
# prueba()
