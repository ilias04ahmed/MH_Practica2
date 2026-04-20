import numpy as np

def penalizacion_consecutivos(sol, mapa_estudiantes):
    p = 0
    for s in mapa_estudiantes:
        exams = mapa_estudiantes[s]
        slots = []
        for e in exams:
            if e in sol:
                slots.append(sol[e][0])
        slots.sort()
        for i in range(len(slots) - 1):
            if slots[i + 1] == slots[i] + 1:
                p += 1
    return p


def penalizacion_mismo_dia(sol, mapa_estudiantes, slots_por_dia=5):
    p = 0
    for s in mapa_estudiantes:
        exams = mapa_estudiantes[s]
        dias = {}
        for e in exams:
            if e in sol:
                slot = sol[e][0]
                dia = slot // slots_por_dia
                if dia not in dias:
                    dias[dia] = 0
                dias[dia] += 1
        for d in dias:
            if dias[d] > 1:
                p += dias[d] - 1
    return p


def penalizacion_distribucion(sol, n_slots):
    uso = [0] * n_slots
    for e in sol:
        slot = sol[e][0]
        uso[slot] += 1
    return np.var(uso)


def incumplimientos(sol, exams, rooms, mapa_estudiantes):
    v = 0

    for i in range(len(exams)):
        exam = int(exams.iloc[i]["exam"])
        n_students = int(exams.iloc[i]["n_students"])
        if exam in sol:
            room = sol[exam][1]
            cap = int(rooms.iloc[room]["capacity"])
            if n_students > cap:
                v += 1

    for s in mapa_estudiantes:
        exams_s = mapa_estudiantes[s]
        slots = []
        for e in exams_s:
            if e in sol:
                slots.append(sol[e][0])
        if len(slots) != len(set(slots)):
            v += 1

    return v


def evaluar_detallado(sol, exams, rooms, mapa_estudiantes, n_slots):
    p1 = penalizacion_consecutivos(sol, mapa_estudiantes)
    p2 = penalizacion_mismo_dia(sol, mapa_estudiantes)
    p3 = penalizacion_distribucion(sol, n_slots)
    v = incumplimientos(sol, exams, rooms, mapa_estudiantes)

    total = p1 + 2 * p2 + p3 + 100000 * v

    return total, p1, p2, p3, v