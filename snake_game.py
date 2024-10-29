import pygame
import time
import random

#Pelicula, no recomendada: es La Sustancia


# Inicializa pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la ventana
ancho_ventana = 600
alto_ventana = 400

# Crea la ventana
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption('Snake Game')

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Tamaño de la serpiente
tamaño_celda = 10
velocidad_serpiente = 15

# Fuente para mostrar puntuaciones
fuente = pygame.font.SysFont('bahnschrift', 25)

def mostrar_puntuacion(puntuacion):
    valor = fuente.render("Puntuación: " + str(puntuacion), True, negro)
    ventana.blit(valor, [0, 0])

def dibujar_serpiente(tamaño_celda, serpiente):
    for x in serpiente:
        pygame.draw.rect(ventana, verde, [x[0], x[1], tamaño_celda, tamaño_celda])

def juego():
    game_over = False
    game_close = False

    x1 = ancho_ventana / 2
    y1 = alto_ventana / 2

    x1_cambio = 0
    y1_cambio = 0

    serpiente = []
    longitud_serpiente = 1

    comida_x = round(random.randrange(0, ancho_ventana - tamaño_celda) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto_ventana - tamaño_celda) / 10.0) * 10.0

    while not game_over:

        while game_close:
            ventana.fill(azul)
            mensaje = fuente.render("Perdiste! Presiona C para continuar o Q para salir", True, rojo)
            ventana.blit(mensaje, [ancho_ventana / 6, alto_ventana / 3])
            mostrar_puntuacion(longitud_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_celda
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_celda
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_celda
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_celda
                    x1_cambio = 0

        if x1 >= ancho_ventana or x1 < 0 or y1 >= alto_ventana or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        ventana.fill(azul)
        pygame.draw.rect(ventana, blanco, [comida_x, comida_y, tamaño_celda, tamaño_celda])
        serpiente.append((x1, y1))

        if len(serpiente) > longitud_serpiente:
            del serpiente[0]

        for x in serpiente[:-1]:
            if x == (x1, y1):
                game_close = True

        dibujar_serpiente(tamaño_celda, serpiente)
        mostrar_puntuacion(longitud_serpiente - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho_ventana - tamaño_celda) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto_ventana - tamaño_celda) / 10.0) * 10.0
            longitud_serpiente += 1

        reloj.tick(velocidad_serpiente)

    pygame.quit()
    quit()

juego()
