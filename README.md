# Práctica 2: Planificación de Exámenes mediante Algoritmos Genéticos - Ilias Ahmed Ahmed

**Asignatura:** Metaheurísticas  
**Grado:** Ingeniería Informática

## Descripción del Proyecto
Este proyecto es la continuación de la resolución del problema clásico de la planificación de exámenes universitarios utilizando técnicas de optimización combinatoria. 
El objetivo es asignar un conjunto de exámenes a diferentes franjas horarias (slots) y aulas (rooms), minimizando un conjunto de penalizaciones (función objetivo) y respetando restricciones duras como la capacidad de las aulas y evitar que un alumno tenga dos exámenes al mismo tiempo.

Para resolverlo en esta segunda iteración, y con el objetivo de escapar de los óptimos locales encontrados por las estrategias basadas en trayectorias de la práctica anterior, he implementado una metaheurística basada en poblaciones:
1. Una **heurística constructiva** para generar una población inicial válida.
2. Dos metaheurísticas basadas en **Búsqueda Local** (recicladas de la P1 para la comparativa):
   - Estrategia de **Primer Mejor** (First Improvement).
   - Estrategia del **Mejor Vecino** (Best Improvement).
3. Un **Algoritmo Genético Generacional** que incluye:
   - Selección por torneo ($k=5$).
   - Cruce Uniforme ($P_c = 0.8$).
   - Mutación conservadora orientada a la diversidad ($P_m = 0.4$).
   - Elitismo ($E=1$) y un criterio de parada inteligente por estancamiento (Early Stopping).

## Estructura del Repositorio
El código está modularizado en los siguientes scripts de Python:

* `main.py`: Script principal que orquesta la ejecución de los experimentos para 3 instancias de distinto tamaño (Pequeña, Media y Grande), ejecutando y comparando el Primer Mejor, el Mejor Vecino y el Algoritmo Genético.
* `generaInstancias.py`: Script para generar instancias sintéticas reproducibles (estudiantes, exámenes, capacidades, aulas).
* `inicial.py`: Contiene la lógica para construir el mapa de estudiantes y generar soluciones iniciales pseudoaleatorias respetando restricciones de aforo.
* `funcionObjetivo.py`: Implementa el cálculo de penalizaciones (exámenes consecutivos, mismo día, mala distribución) y los incumplimientos de restricciones duras.
* `busquedaLocal.py`: Implementa la generación de vecindarios y los algoritmos de Búsqueda Local (Primer Mejor y Mejor Vecino).
* `algoritmoGenetico.py`: Implementa el bucle principal del Algoritmo Genético, junto con sus funciones de selección, cruce y mutación.
* `graficas.py`: Funciones auxiliares para generar las curvas de convergencia comparativas y las gráficas de tiempos/costes que ilustran el rendimiento de cada algoritmo.

## Requisitos y Dependencias
El proyecto está desarrollado íntegramente en Python. Solo hace uso de librerías estándar y de análisis/visualización de datos. No se utilizan librerías externas de optimización algorítmica.

Para ejecutar el código, necesitas instalar las siguientes dependencias:
```bash
pip install numpy pandas matplotlib
```

Y basta con ejecutar el script principal:
```bash
python main.py
```