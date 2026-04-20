import random
from inicial import solucion_inicial
from funcionObjetivo import evaluar_detallado

def seleccion_torneo(pob_evaluada, k):
    participantes = random.sample(pob_evaluada, k)
    participantes.sort(key=lambda x: x[1])
    return participantes[0][0]

def cruce_uniforme(padre1, padre2):
    hijo1 = {}
    hijo2 = {}
    
    for examen in padre1.keys():
        if random.random() < 0.5:
            hijo1[examen] = padre1[examen]
            hijo2[examen] = padre2[examen]
        else:
            hijo1[examen] = padre2[examen]
            hijo2[examen] = padre1[examen]
            
    return hijo1, hijo2

def mutacion(individuo, exams, rooms, n_slots, prob):
    mutante = individuo.copy()
    
    if random.random() < prob:
        examen_mutar = random.choice(list(mutante.keys()))
        nuevo_slot = random.randint(0, n_slots - 1)
        nueva_aula = random.randint(0, len(rooms) - 1)
        
        mutante[examen_mutar] = (nuevo_slot, nueva_aula)
        
    return mutante

def algoritmo_genetico(exams, rooms, mapa_estud, n_slots, n_pob=60, n_gen=200, max_sin_mejora=20, prob_cruce=0.8, prob_mutacion=0.4):
    pob = [solucion_inicial(exams, rooms, n_slots) for _ in range(n_pob)]
    historial_evolucion = []
    
    mejor_historico_coste = float('inf')
    generaciones_sin_mejora = 0
    mejor_actual_completo = None

    for gen in range(n_gen):
        pob_evaluada = [(ind, evaluar_detallado(ind, exams, rooms, mapa_estud, n_slots)[0]) for ind in pob]
        pob_evaluada.sort(key=lambda x: x[1])
        
        mejor_actual = pob_evaluada[0]
        historial_evolucion.append(mejor_actual[1])
        
        if mejor_actual[1] < mejor_historico_coste:
            mejor_historico_coste = mejor_actual[1]
            mejor_actual_completo = mejor_actual[0].copy()
            generaciones_sin_mejora = 0 
        else:
            generaciones_sin_mejora += 1 
            
        if generaciones_sin_mejora >= max_sin_mejora:
            print(f"   -> [Info] AG detenido en la generacion {gen} por estancamiento.")
            break

        nueva_pob = [mejor_actual[0].copy()]
        
        while len(nueva_pob) < n_pob:
            padre1 = seleccion_torneo(pob_evaluada, k=5)
            padre2 = seleccion_torneo(pob_evaluada, k=5)
            
            if random.random() < prob_cruce:
                hijo1, hijo2 = cruce_uniforme(padre1, padre2)
            else:
                hijo1, hijo2 = padre1.copy(), padre2.copy()
            
            nueva_pob.append(mutacion(hijo1, exams, rooms, n_slots, prob_mutacion))
            
            if len(nueva_pob) < n_pob:
                nueva_pob.append(mutacion(hijo2, exams, rooms, n_slots, prob_mutacion))
                
        pob = nueva_pob
        
    return mejor_actual_completo, mejor_historico_coste, historial_evolucion