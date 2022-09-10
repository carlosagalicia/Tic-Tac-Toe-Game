"""
Avance del proyecto python
Juego de Gato
El programa actual abre una ventana de ancho y alto definidos,
dividiendo su ancho y alto entre 3 para poder desplegar las lineas
que conforman el area de juego uniformemente, a distancias iguales y
a coordenadas definidas en la ventana. Esto mediante operadores como
"//", "*" y "-". Ademas de esto, se utilizan funciones para poder identificar el tipo de símbolo y el cuadrante en el
que se encuentra este ultimo, esto con el objetivo de colocar el símbolo en el cuadrante correspondiente del area de juego.
"""
# Bibliotecas
import pygame
"""
================================ funciones de dibujo =======================================
"""


def dibujar_gato(ventana, blanco, alto, ancho):
    """
    (uso de funciones)
    recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos, "alto" valor numerico,
    "ancho" valor numerico
    Dibuja las 4 lineas blancas que integraran el area de juego de gato
    devuelve: no devuelve ningun valor
    """
    pygame.draw.line(ventana, blanco, (ancho // 3, alto), ((ancho // 3), (alto * -1)), 3)
    pygame.draw.line(ventana, blanco, ((ancho // 3)*2, alto), ((ancho // 3)*2, (alto * -1)), 3)
    pygame.draw.line(ventana, blanco, (ancho, alto // 3), (ancho * -1, alto // 3), 3)
    pygame.draw.line(ventana, blanco, (ancho, (alto // 3)*2), (ancho * -1, (alto // 3)*2), 3)


def dibujar_cruz(ventana, blanco, c_x, c_y):
    """
    (uso de funciones)
    (uso de operadores numericos)
    recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos, "c_x" valor numerico,
    "c_y" valor numerico
    Dibuja 2 lineas cruzadas color blanco que integran el simbolo de la cruz
    devuelve: no devuelve ningun valor
    """
    pygame.draw.line(ventana, blanco, (c_x + 80, c_y + 80), (c_x - 80, c_y - 80), 3)
    pygame.draw.line(ventana, blanco, (c_x + 80, c_y - 80), (c_x - 80, c_y + 80), 3)


def dibujar_circulo(ventana, blanco, c_x, c_y):
    """
    (uso de funciones)
    (uso de operadores numericos)
    recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos, "c_x" valor numerico,
    "c_y" valor numerico
    Dibuja un circulo blanco que representa al simbolo del circulo
    devuelve: no devuelve ningun valor
    """
    pygame.draw.circle(ventana, blanco, (c_x, c_y), 80, 3)


"""
================================ funcion de clasificacion =======================================
"""


def clasificar(ventana, blanco):
    """
    (uso de funciones)
    (uso de estructuras condicionales)
    recibe: "ventana" valor clase pygame.Surface, "blanco" tupla de valores numericos
    Asigna las coordenadas c_x y c_y (donde se dibujaran la cruz o el circulo) y el numero de cuadrante dependiendo
    de las coordenadas donde el mouse haya hecho click. Ademas cambia el simbolo cruz o circulo por turnos.
    Devuelve: el cuadrante donde se hizo click y la forma colocada
    """
    global forma
    forma_colocada = ""
    c_x = 0
    c_y = 0
    cuadrante = 0
    pos = pygame.mouse.get_pos()
    if 0 <= pos[1] < 200:
        c_y = 100
        if 0 <= pos[0] < 200:
            c_x = 100
            cuadrante = 1

        elif 200 <= pos[0] < 400:
            c_x = 300
            cuadrante = 2

        elif 400 <= pos[0] <= 600:
            c_x = 500
            cuadrante = 3

    elif 200 <= pos[1] < 400:
        c_y = 300
        if 0 <= pos[0] < 200:
            c_x = 100
            cuadrante = 4
        elif 200 <= pos[0] < 400:
            c_x = 300
            cuadrante = 5
        elif 400 <= pos[0] <= 600:
            c_x = 500
            cuadrante = 6

    elif 400 <= pos[1] <= 600:
        c_y = 500
        if 0 <= pos[0] < 200:
            c_x = 100
            cuadrante = 7
        elif 200 <= pos[0] < 400:
            c_x = 300
            cuadrante = 8
        elif 400 <= pos[0] <= 600:
            c_x = 500
            cuadrante = 9

    if forma == "x":
        dibujar_cruz(ventana, blanco, c_x, c_y)
        forma_colocada = "x"
        forma = "o"
    else:
        dibujar_circulo(ventana, blanco, c_x, c_y)
        forma_colocada = "o"
        forma = "x"
    return cuadrante, forma_colocada


"""
================================ funcion principal main =======================================
"""


def main():
    """
    (uso de funciones, condicionales)
    (uso de estructuras condicionales)
    (uso de estructuras cíclicas for y while)
    recibe: ningun valor
    Despliega la ventana de juego, dibuja el mapa de juego y utiliza estructuras while y for para leer cada evento
    y si el tipo de evento es un click llama a la funcion que retorna la figura y el numero de cuadrante donde se coloco.
    Si se detecta un evento de salida, el ciclo while que antes era verdadero y actualizaba la ventana
    se convierte en falso y termina el programa.
    devuelve: ningun valor
    """
    ancho = 600
    alto = 600
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    estado = True

    # Ventana
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    print(type(ventana))
    dibujar_gato(ventana, blanco, alto, ancho)

    while estado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                cuadrante = clasificar(ventana, blanco)
                print(cuadrante)

        pygame.display.flip()
    pygame.quit()


"""
================================ parte principal del programa =======================================
"""
forma = "x"
main()
