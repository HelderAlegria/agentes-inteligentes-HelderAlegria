import random
import time

TAMANO_CUADRÍCULA = 5

def crear_cuadricula():
    return [['.' for _ in range(TAMANO_CUADRÍCULA)] for _ in range(TAMANO_CUADRÍCULA)]

def mostrar_cuadricula(cuadricula):
    for fila in cuadricula:
        print(" ".join(fila))
    print()

def colocar_elementos():
   x_objeto = random.randint(0, TAMANO_CUADRÍCULA - 1)
    y_objeto = random.randint(0, TAMANO_CUADRÍCULA - 1)

    x_agente = random.randint(0, TAMANO_CUADRÍCULA - 1)
    y_agente = random.randint(0, TAMANO_CUADRÍCULA - 1)

    while x_agente == x_objeto and y_agente == y_objeto:
        x_agente = random.randint(0, TAMANO_CUADRÍCULA - 1)
        y_agente = random.randint(0, TAMANO_CUADRÍCULA - 1)

    return (x_objeto, y_objeto), (x_agente, y_agente)

def mover_agente(x_agente, y_agente, x_objeto, y_objeto):
    if x_agente < x_objeto:
        x_agente += 1
    elif x_agente > x_objeto:
        x_agente -= 1
    elif y_agente < y_objeto:
        y_agente += 1
    elif y_agente > y_objeto:
        y_agente -= 1
    return x_agente, y_agente

def buscar_objeto():
    (x_objeto, y_objeto), (x_agente, y_agente) = colocar_elementos()

    cuadricula = crear_cuadricula()

    while (x_agente, y_agente) != (x_objeto, y_objeto):
        cuadricula = crear_cuadricula()
        cuadricula[x_agente][y_agente] = 'A'  
        cuadricula[x_objeto][y_objeto] = 'O'  

        mostrar_cuadricula(cuadricula)

        x_agente, y_agente = mover_agente(x_agente, y_agente, x_objeto, y_objeto)

        time.sleep(0.5)

    cuadricula[x_agente][y_agente] = 'A'
    cuadricula[x_objeto][y_objeto] = 'O'
    mostrar_cuadricula(cuadricula)
    print("¡El agente ha encontrado el objeto!")

buscar_objeto()
