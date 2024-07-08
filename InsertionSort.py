# Ejercicio de Insertion Sort

# Creamos la función
def insertionSort(lista):
    # Iteramos sobre los elementos de la lista empezando por el segundo elemento
    for i in range(1, len(lista)):
        # Guardamos el valor actual
        valor_actual = lista[i]
        # Inicializamos la posición actual
        posicion = i

        # Iteramos sobre los elementos anteriores y los movemos una posición hacia adelante
        # si son mayores que el valor actual
        while posicion > 0 and lista[posicion - 1] > valor_actual:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1

        # Colocamos el valor actual en la posición correcta
        lista[posicion] = valor_actual

    # Retornamos la lista ordenada
    return lista

# Ejemplo de uso del algoritmo insertion sort
print(insertionSort([3, 4, 9, 2, 1, 8, 5, 7, 6]))
