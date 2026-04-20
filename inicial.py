import random

def construir_mapa_estudiantes(student_exam):
    mapa = {}
    for i in range(len(student_exam)):
        s = int(student_exam.iloc[i]["student"])
        e = int(student_exam.iloc[i]["exam"])
        if s not in mapa:
            mapa[s] = []
        mapa[s].append(e)
    return mapa


def solucion_inicial(exams, rooms, n_slots):
    sol = {}
    for i in range(len(exams)):
        exam = int(exams.iloc[i]["exam"])
        n_students = int(exams.iloc[i]["n_students"])

        asignado = False
        intentos = 0

        while not asignado and intentos < 100:
            slot = random.randint(0, n_slots - 1)
            room = random.randint(0, len(rooms) - 1)
            cap = int(rooms.iloc[room]["capacity"])

            if n_students <= cap:
                sol[exam] = (slot, room)
                asignado = True
            intentos += 1

        if not asignado:
            sol[exam] = (random.randint(0, n_slots - 1), 0)

    return sol