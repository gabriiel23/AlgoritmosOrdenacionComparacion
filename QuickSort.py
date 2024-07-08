# Ejercicio de Quick Sort

# Creamos la función principal de Quick Sort
def quickSort(lista):
    # Llamamos a la función auxiliar que implementa Quick Sort
    quickSortHelper(lista, 0, len(lista) - 1)
    return lista

# Función auxiliar que implementa el algoritmo de Quick Sort
def quickSortHelper(lista, primero, ultimo):
    if primero < ultimo:
        # Obtenemos el punto de partición
        punto_particion = particion(lista, primero, ultimo)

        # Ordenamos recursivamente las dos mitades
        quickSortHelper(lista, primero, punto_particion - 1)
        quickSortHelper(lista, punto_particion + 1, ultimo)

# Función que realiza la partición de la lista
def particion(lista, primero, ultimo):
    # Elegimos el pivote como el primer elemento de la lista
    pivote = lista[primero]

    # Inicializamos los índices para la partición
    izquierda = primero + 1
    derecha = ultimo

    hecho = False
    while not hecho:
        # Movemos el índice izquierdo hacia la derecha hasta encontrar un valor mayor que el pivote
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda + 1

        # Movemos el índice derecho hacia la izquierda hasta encontrar un valor menor que el pivote
        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha = derecha - 1

        # Si los índices se cruzan, terminamos el bucle
        if derecha < izquierda:
            hecho = True
        else:
            # Si no se cruzan, intercambiamos los elementos
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

    # Intercambiamos el pivote con el elemento en el índice derecho
    lista[primero], lista[derecha] = lista[derecha], lista[primero]

    # Retornamos el punto de partición
    return derecha

# Ejemplo de uso del algoritmo quick sort
print(quickSort([3, 4, 9, 2, 1, 8, 5, 7, 6]))
