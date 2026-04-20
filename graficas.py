import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("graficas", exist_ok=True)

def grafica_convergencia(evolucion_pm, evolucion_mm, evolucion_ag, nombre="Instancia Media"):
    plt.figure(figsize=(10, 6))
    
    plt.plot(evolucion_pm, label='Primer Mejor', color='blue', linewidth=2)
    plt.plot(evolucion_mm, label='Mejor Vecino', color='red', linestyle='--', linewidth=2)
    plt.plot(evolucion_ag, label='Algoritmo Genetico', color='green', linestyle='-.', linewidth=2)
    
    plt.title("Curva de Convergencia - " + nombre, fontsize=14)
    plt.xlabel("Iteraciones / Generaciones", fontsize=12)
    plt.ylabel("Coste Total", fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    nombre_limpio = nombre.replace(" ", "_").replace("(", "").replace(")", "")
    ruta = f"graficas/convergencia_{nombre_limpio}.png"
    
    plt.savefig(ruta, dpi=300, bbox_inches='tight')
    plt.close()


def graficas_comparativas(nombres, costes_pm, costes_mm, costes_ag, tiempos_pm, tiempos_mm, tiempos_ag):
    x = np.arange(len(nombres))
    ancho = 0.25
    
    # Grafica de costes
    plt.figure(figsize=(10, 6))
    plt.bar(x - ancho, costes_pm, ancho, label='Primer Mejor', color='blue')
    plt.bar(x, costes_mm, ancho, label='Mejor Vecino', color='red')
    plt.bar(x + ancho, costes_ag, ancho, label='Algoritmo Genetico', color='green')
    
    plt.title("Comparativa de Coste Final por Tamaño de Instancia", fontsize=14)
    plt.ylabel("Coste Total", fontsize=12)
    plt.xticks(x, nombres)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.savefig("graficas/comparativa_costes.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    # Grafica de tiempos
    plt.figure(figsize=(10, 6))
    plt.bar(x - ancho, tiempos_pm, ancho, label='Primer Mejor', color='blue')
    plt.bar(x, tiempos_mm, ancho, label='Mejor Vecino', color='red')
    plt.bar(x + ancho, tiempos_ag, ancho, label='Algoritmo Genetico', color='green')
    
    plt.title("Comparativa de Tiempos de Ejecucion", fontsize=14)
    plt.ylabel("Tiempo (Segundos)", fontsize=12)
    plt.xticks(x, nombres)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    
    plt.savefig("graficas/comparativa_tiempos.png", dpi=300, bbox_inches='tight')
    plt.close()


def histograma_alumnos(exams, nombre="Instancia Media"):
    plt.figure(figsize=(10, 6))
    
    alumnos = exams["n_students"].tolist()
    
    plt.hist(alumnos, bins=15, color='green', edgecolor='black', alpha=0.7)
    
    plt.title("Distribucion de Alumnos por Examen - " + nombre, fontsize=14)
    plt.xlabel("Numero de alumnos matriculados", fontsize=12)
    plt.ylabel("Cantidad de examenes", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig(f"graficas/histograma_alumnos_{nombre.replace(' ', '_')}.png", dpi=300, bbox_inches='tight')
    plt.close()