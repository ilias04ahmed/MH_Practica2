import time
import matplotlib.pyplot as plt

from algoritmoGenetico import algoritmo_genetico
from generaInstancias import generar_instancia 
from inicial import construir_mapa_estudiantes

def realizar_experimentos_parametros():
    print("Iniciando experimentos de parametros...")
    
    # Generamos una instancia pequeña para que las pruebas no tarden una eternidad
    student_exam, exams, rooms, n_slots = generar_instancia(
        n_exams=50, 
        n_students=1000, 
        n_rooms=5, 
        n_slots=25, 
        seed=42
    )
    mapa_estudiantes = construir_mapa_estudiantes(student_exam)

    print("\n--- Experimento 1: Tamaño de Poblacion ---")
    poblaciones = [10, 50, 100]
    resultados_pob = {}
    plt.figure(figsize=(10, 6))
    
    for n in poblaciones:
        print(f"Probando N = {n}...")
        inicio = time.time()
        _, coste, historial = algoritmo_genetico(
            exams, rooms, mapa_estudiantes, n_slots, 
            n_pob=n, n_gen=50, max_sin_mejora=50, 
            prob_cruce=0.8, prob_mutacion=0.1
        )
        fin = time.time()
        resultados_pob[n] = (coste, fin - inicio)
        plt.plot(historial, label=f'N = {n}')
    
    plt.title('Convergencia segun tamaño de Poblacion (N)')
    plt.xlabel('Generaciones')
    plt.ylabel('Coste (Fitness)')
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/exp_poblacion.png')
    plt.close()
    
    print("\n--- Experimento 2: Probabilidad de Cruce ---")
    prob_cruces = [0.0, 0.4, 0.8, 1.0]
    resultados_cruce = {}
    plt.figure(figsize=(10, 6))
    
    for pc in prob_cruces:
        print(f"Probando Pc = {pc}...")
        _, coste, historial = algoritmo_genetico(
            exams, rooms, mapa_estudiantes, n_slots, 
            n_pob=50, n_gen=50, max_sin_mejora=50, 
            prob_cruce=pc, prob_mutacion=0.1
        )
        resultados_cruce[pc] = coste
        plt.plot(historial, label=f'Pc = {pc}')
        
    plt.title('Convergencia segun Probabilidad de Cruce (Pc)')
    plt.xlabel('Generaciones')
    plt.ylabel('Coste (Fitness)')
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/exp_cruce.png')
    plt.close()

    print("\n--- Experimento 3: Probabilidad de Mutacion ---")
    prob_mutaciones = [0.01, 0.1, 0.5]
    resultados_mutacion = {}
    plt.figure(figsize=(10, 6))
    
    for pm in prob_mutaciones:
        print(f"Probando Pm = {pm}...")
        _, coste, historial = algoritmo_genetico(
            exams, rooms, mapa_estudiantes, n_slots, 
            n_pob=50, n_gen=50, max_sin_mejora=50, 
            prob_cruce=0.8, prob_mutacion=pm
        )
        resultados_mutacion[pm] = coste
        plt.plot(historial, label=f'Pm = {pm}')
        
    plt.title('Convergencia segun Probabilidad de Mutacion (Pm)')
    plt.xlabel('Generaciones')
    plt.ylabel('Coste (Fitness)')
    plt.legend()
    plt.grid(True)
    plt.savefig('graficas/exp_mutacion.png')
    plt.close()
    
    print("\n=== RESUMEN ===")
    print("1. POBLACION (Pc=0.8, Pm=0.1)")
    for n, (coste, tiempo) in resultados_pob.items():
        print(f"   N={n} -> Coste: {coste:.2f} | Tiempo: {tiempo:.2f}s")
        
    print("\n2. CRUCE (N=50, Pm=0.1)")
    for pc, coste in resultados_cruce.items():
        print(f"   Pc={pc} -> Coste: {coste:.2f}")
        
    print("\n3. MUTACION (N=50, Pc=0.8)")
    for pm, coste in resultados_mutacion.items():
        print(f"   Pm={pm} -> Coste: {coste:.2f}")

if __name__ == "__main__":
    realizar_experimentos_parametros()