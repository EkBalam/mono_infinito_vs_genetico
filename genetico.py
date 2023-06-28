import random
from tqdm import tqdm

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

def cruza(cadena1, cadena2):
    punto_cruza = random.randint(0, len(cadena1))
    cadena_hijo1 = cadena1[0:punto_cruza] + cadena2[punto_cruza:]
    cadena_hijo2 = cadena2[0:punto_cruza] + cadena1[punto_cruza:]
    return cadena_hijo1, cadena_hijo2

def mutacion(cadena, probMutar):
    cadenaM = list(cadena)
    for i in range(len(cadena)):
        cadenaM[i] = chr(random.randint(97, 122)) if random.random() < probMutar else cadenaM[i]
    return "".join(cadenaM)


def crear_poblacion(tamano, original):
    poblacion = []
    for _ in range(tamano):
        palabra = palabra_aleatoria(len(original))
        poblacion.append(
            {
                "cadena": palabra,
                "fitness": comparar_cadenas(original, palabra)/len(original)
            }
        )
    return poblacion

def seleccion_padres(poblacion):
    padres = []
    while len(padres) < len(poblacion):
        for individuo in poblacion:
            fit = 0.1 if individuo['fitness'] == 0 else individuo['fitness']
            if random.random() < fit:
                padres.append(individuo)
    return padres

def estadisticas(poblacion):
    mejor = poblacion[0]
    peor = poblacion[0]
    suma_fit = 0
    for individuo in poblacion:
        mejor = individuo if individuo['fitness'] >= mejor['fitness'] else mejor
        peor = individuo if individuo['fitness'] <= peor['fitness'] else peor
        suma_fit += individuo['fitness']
    return mejor, peor, suma_fit/len(poblacion)

# individuo = {
#     "cadena": "",
#     "puntuacion": 0
# }

# print(cruza("holamundo", "mundohola"))
# print(mutacion("holamundo", 0.2))
# pop = crear_poblacion(5, "holamundo")
# print(pop)
# print(seleccion_padres(pop))

prob_cruza = 1.0
prob_mutar = 0.1
generaciones = 100
tam_pop = 100
objetivo = "holamundo"

for _ in range(30):
    poblacion = crear_poblacion(tam_pop, objetivo)
    pbar = tqdm(range(generaciones))
    for g in pbar:
        mejor, peor, prom_fit = estadisticas(poblacion)
        pbar.set_description("{:.0f} {:.2f} {:.2f}".format(g, mejor['fitness'], prom_fit))

        if(mejor['fitness'] == 1):
            break
    
        padres = seleccion_padres(poblacion)
        
        siguiente_generacion = []
        for p in range(0, tam_pop, 2):
            hijo1 = {}
            hijo2 = {}
            if random.random() < prob_cruza:
                cadena_hijo1, cadena_hijo2 = cruza(padres[p]['cadena'], padres[p+1]['cadena'])
                hijo1 = {"cadena": cadena_hijo1, "fitness":0 }
                hijo2 = {"cadena": cadena_hijo2, "fitness":0 }
                #print(p, hijo1, hijo2)
            else:
                hijo1 = padres[p]
                hijo2 = padres[p+1]
            
            hijo1['cadena'] = mutacion(hijo1['cadena'], prob_mutar)
            hijo2['cadena'] = mutacion(hijo2['cadena'], prob_mutar)
            hijo1['fitness'] = comparar_cadenas(objetivo, hijo1['cadena'])/len(objetivo)
            hijo2['fitness'] = comparar_cadenas(objetivo, hijo2['cadena'])/len(objetivo)
            siguiente_generacion.append(hijo1)
            siguiente_generacion.append(hijo2)

        poblacion = siguiente_generacion
        poblacion[0] = mejor

#print(estadisticas(poblacion))