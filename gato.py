"""
Avance del proyecto python
Juego de Gato
El programa actual abre una ventana de ancho y alto definidos,
dividiendo su ancho y alto entre 3 para poder desplegar las lineas
que conforman el area de juego uniformemente, a distancias iguales y
a coordenadas definidas en la ventana. Esto mediante operadores como
"//", "*" y "-"

"""

import time
import pygame


"""
================================ parte principal del programa =======================================
"""


def main():
    # Se inicializan las variables que determinan algunos colores y las medidas de la ventana
    """
    (manejo de variables y tipos)
    """
    ancho = 600
    alto = 600
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    estado = True


    # Inicializar proceso de la librería y ventana con sus medidas
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))

    # Dibujar gato
    """
    (manejo de operadores)
    """
    pygame.draw.line(ventana, blanco, (ancho // 3, alto), ((ancho // 3), (alto * -1)), 3)
    pygame.draw.line(ventana, blanco, ((ancho // 3) * 2, alto), ((ancho // 3) * 2, (alto * -1)), 3)
    pygame.draw.line(ventana, blanco, (ancho, alto // 3), (ancho * -1, alto // 3), 3)
    pygame.draw.line(ventana, blanco, (ancho, (alto // 3) * 2), (ancho * -1, (alto // 3) * 2), 3)

    # Mientras que el usuario no cierre la ventana se actualizará la misma
    while estado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = False
        pygame.display.flip()

    # Termina el proceso de la librería
    pygame.quit()


main()
