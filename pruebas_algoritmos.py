import time
import sys

# Incrementamos el límite de recursión
sys.setrecursionlimit(2000)

# Importar los algoritmos de ordenamiento
from BubbleSort import bubble
from InsertionSort import insertionSort
from MergeSort import mergeSort
from QuickSort import quickSort
from SelectionSort import selectionSort

# Datos de prueba
datasets = {
    "Pequeño y ordenado": list(range(10)),
    "Pequeño y desordenado": [3, 5, 1, 2, 9, 7, 4, 8, 6, 0],
    "Grande y ordenado": list(range(1000)),
    "Grande y desordenado": list(range(999, -1, -1))
}

# Función para medir el tiempo de ejecución
def medir_tiempo(func, lista):
    inicio = time.time()
    func(lista.copy())
    fin = time.time()
    return fin - inicio

# Algoritmos de ordenamiento
algoritmos = {
    "Bubble Sort": bubble,
    "Insertion Sort": insertionSort,
    "Merge Sort": mergeSort,
    "Quick Sort": quickSort,
    "Selection Sort": selectionSort
}

# Ejecución de pruebas
resultados = {}
for nombre, algoritmo in algoritmos.items():
    resultados[nombre] = {}
    for descripcion, datos in datasets.items():
        tiempo = medir_tiempo(algoritmo, datos)
        resultados[nombre][descripcion] = tiempo

# Mostrar resultados
for nombre, tiempos in resultados.items():
    print(f"\nAlgoritmo: {nombre}")
    for descripcion, tiempo in tiempos.items():
        print(f"  {descripcion}: {tiempo:.6f} segundos")
