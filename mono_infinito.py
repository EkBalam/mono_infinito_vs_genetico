
# Mayusculas 65-90
# Minusculas 97-122
import random

def comparar_cadenas(original, mono):
    puntuacion = 0
    for i in range(len(original)):
        puntuacion += 1 if original[i] == mono[i] else 0
    return puntuacion

def palabra_aleatoria(longitud):
    palabra = ""
    for _ in range(longitud):
        palabra += chr(random.randint(97, 122))
    return palabra


cadena_objetivo = "holamundo"

letra = random.randint(65, 90)


print(letra, chr(letra))
maximo = 0
palabra_max = ""
g = 0
while(True):
    palabra = palabra_aleatoria(len(cadena_objetivo))

    puntuacion = comparar_cadenas(cadena_objetivo, palabra)
    if puntuacion > maximo:
        maximo = puntuacion
        palabra_max = palabra
    print(g, maximo, palabra_max, cadena_objetivo, palabra, puntuacion)
    if puntuacion == len(cadena_objetivo):
        break
    g += 1
