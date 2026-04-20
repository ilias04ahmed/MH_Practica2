import random
from funcionObjetivo import evaluar_detallado

def generar_vecino(sol, exams, rooms, n_slots):
    nuevo = dict(sol)
    tipo = random.randint(0, 2)

    if tipo == 0 or tipo == 1:
        exam = random.choice(list(nuevo.keys()))
        slot_actual, room_actual = nuevo[exam]

        if tipo == 0:
            nuevo_slot = random.randint(0, n_slots - 1)
            nuevo[exam] = (nuevo_slot, room_actual)
        else:
            nueva_room = random.randint(0, len(rooms) - 1)
            nuevo[exam] = (slot_actual, nueva_room)
    else:
        e1, e2 = random.sample(list(nuevo.keys()), 2)
        nuevo[e1], nuevo[e2] = nuevo[e2], nuevo[e1]

    return nuevo


def busqueda_primer_mejor(sol, exams, rooms, mapa_estudiantes, n_slots, max_iter=5000):
    actual = dict(sol)
    coste_actual, _, _, _, _ = evaluar_detallado(actual, exams, rooms, mapa_estudiantes, n_slots)

    evaluaciones = 0
    mejora = True
    evolucion = [coste_actual]

    while mejora and evaluaciones < max_iter:
        mejora = False
        for _ in range(500):
            vecino = generar_vecino(actual, exams, rooms, n_slots)
            coste_vecino, _, _, _, _ = evaluar_detallado(vecino, exams, rooms, mapa_estudiantes, n_slots)
            evaluaciones += 1

            if coste_vecino < coste_actual:
                actual = vecino
                coste_actual = coste_vecino
                evolucion.append(coste_actual)
                mejora = True
                break

    return actual, coste_actual, evaluaciones, evolucion


def busqueda_mejor(sol, exams, rooms, mapa_estudiantes, n_slots, max_iter=5000):
    actual = dict(sol)
    coste_actual, _, _, _, _ = evaluar_detallado(actual, exams, rooms, mapa_estudiantes, n_slots)

    evaluaciones = 0
    mejora = True
    evolucion = [coste_actual]

    while mejora and evaluaciones < max_iter:
        mejor_vecino = None
        mejor_coste = coste_actual

        for _ in range(500):
            vecino = generar_vecino(actual, exams, rooms, n_slots)
            coste_vecino, _, _, _, _ = evaluar_detallado(vecino, exams, rooms, mapa_estudiantes, n_slots)
            evaluaciones += 1

            if coste_vecino < mejor_coste:
                mejor_vecino = vecino
                mejor_coste = coste_vecino

        if mejor_vecino is not None:
            actual = mejor_vecino
            coste_actual = mejor_coste
            evolucion.append(coste_actual)
        else:
            mejora = False

    return actual, coste_actual, evaluaciones, evolucion