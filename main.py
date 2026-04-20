import time

from generaInstancias import generar_instancia
from inicial import construir_mapa_estudiantes, solucion_inicial
from funcionObjetivo import evaluar_detallado
from busquedaLocal import busqueda_primer_mejor, busqueda_mejor
from algoritmoGenetico import algoritmo_genetico
from graficas import grafica_convergencia, graficas_comparativas, histograma_alumnos

def imprimir_detalle(nombre, sol, exams, rooms, mapa_estudiantes, n_slots, tiempo, evaluaciones, evolucion):
    total, p1, p2, p3, v = evaluar_detallado(sol, exams, rooms, mapa_estudiantes, n_slots)

    print(f"------ {nombre} ------")
    print("Coste total:", round(total, 2))
    print(" Penalizacion consecutivos:", p1)
    print(" Penalizacion mismo dia:", p2)
    print(" Penalizacion distribucion:", round(p3, 2))
    print(" Incumplimientos:", v)
    print(" Tiempo:", round(tiempo, 4), "segundos")
    print(" Evaluaciones:", evaluaciones)
    print(" Iteraciones (mejoras):", len(evolucion) - 1)
    print()

def ejecutar_experimentos():
    nombres_instancias = []
    costes_pm = []
    costes_mm = []
    costes_ag = []
    tiempos_pm = []
    tiempos_mm = []
    tiempos_ag = []

    exams_media = None

    casos_exams = [50, 100, 200]
    casos_students = [1000, 2000, 4000]
    casos_rooms = [5, 10, 20]
    casos_slots = [25, 40, 100]
    nombres = ["Pequeña (50 ex)", "Media (100 ex)", "Grande (200 ex)"]

    for i in range(3):
        print("\n========================================================")
        print(f" EJECUTANDO INSTANCIA: {nombres[i]}")
        print("========================================================")

        student_exam, exams, rooms, n_slots = generar_instancia(
            n_exams=casos_exams[i], 
            n_students=casos_students[i], 
            n_rooms=casos_rooms[i], 
            n_slots=casos_slots[i], 
            seed=42
        )
        mapa_estudiantes = construir_mapa_estudiantes(student_exam)

        print("Examenes:", len(exams))
        print("Estudiantes:", len(mapa_estudiantes))
        print("Aulas:", len(rooms))
        print("Slots:", n_slots)
        print()

        inicio = time.time()
        sol_ini = solucion_inicial(exams, rooms, n_slots)
        t_ini = time.time() - inicio

        total_ini, p1_ini, p2_ini, p3_ini, v_ini = evaluar_detallado(sol_ini, exams, rooms, mapa_estudiantes, n_slots)

        print("------ SOLUCION INICIAL ------")
        print("Coste total:", round(total_ini, 2))
        print(" Incumplimientos:", v_ini)
        print(" Tiempo:", round(t_ini, 4), "segundos")
        print()

        inicio = time.time()
        sol_pm, coste_pm, eval_pm, evo_pm = busqueda_primer_mejor(
            sol_ini, exams, rooms, mapa_estudiantes, n_slots
        )
        t_pm = time.time() - inicio

        imprimir_detalle(
            "BUSQUEDA PRIMER MEJOR",
            sol_pm, exams, rooms, mapa_estudiantes, n_slots,
            t_pm, eval_pm, evo_pm
        )

        inicio = time.time()
        sol_mm, coste_mm, eval_mm, evo_mm = busqueda_mejor(
            sol_ini, exams, rooms, mapa_estudiantes, n_slots
        )
        t_mm = time.time() - inicio

        imprimir_detalle(
            "BUSQUEDA MEJOR VECINO",
            sol_mm, exams, rooms, mapa_estudiantes, n_slots,
            t_mm, eval_mm, evo_mm
        )

        inicio = time.time()
        sol_ag, coste_ag, evo_ag = algoritmo_genetico(
            exams, rooms, mapa_estudiantes, n_slots
        )
        t_ag = time.time() - inicio
        
        eval_ag = 50 * len(evo_ag) 
        
        imprimir_detalle(
            "ALGORITMO GENETICO",
            sol_ag, exams, rooms, mapa_estudiantes, n_slots,
            t_ag, eval_ag, evo_ag
        )

        grafica_convergencia(evo_pm, evo_mm, evo_ag, nombres[i])

        nombres_instancias.append(nombres[i])
        costes_pm.append(coste_pm)
        costes_mm.append(coste_mm)
        costes_ag.append(coste_ag)
        tiempos_pm.append(t_pm)
        tiempos_mm.append(t_mm)
        tiempos_ag.append(t_ag)

        if i == 1:
            exams_media = exams

    print("\n\n-------------------------------------------------------------------------------------------------------------------------")
    print(" TABLA RESUMEN")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Instancia\t\tCoste PM\tCoste MV\tCoste AG\tTiempo PM\tTiempo MV\tTiempo AG")
    print("-------------------------------------------------------------------------------------------------------------------------")
    
    for i in range(3):
        nombre_str = nombres_instancias[i]
        
        if len(nombre_str) < 16:
            nombre_str += "\t"
            
        c_pm = round(costes_pm[i], 2)
        c_mm = round(costes_mm[i], 2)
        c_ag = round(costes_ag[i], 2)
        t_pm = round(tiempos_pm[i], 2)
        t_mm = round(tiempos_mm[i], 2)
        t_ag = round(tiempos_ag[i], 2)
        
        print(f"{nombre_str}\t{c_pm}\t{c_mm}\t{c_ag}\t{t_pm} s\t\t{t_mm} s\t\t{t_ag} s")
        
    print("-------------------------------------------------------------------------------------------------------------------------\n")

    graficas_comparativas(nombres_instancias, costes_pm, costes_mm, costes_ag, tiempos_pm, tiempos_mm, tiempos_ag)
    histograma_alumnos(exams_media, "Instancia Media")
    
    print("Ejecucion terminada. Graficas guardadas.")

if __name__ == "__main__":
    ejecutar_experimentos()