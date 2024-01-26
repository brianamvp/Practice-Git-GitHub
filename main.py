def ordenar_numeros (lista): 
    lista.sort()
    return lista

numeros = [3, 4, 1, 9, 2, 6, 5]
numeros_ordenados = ordenar_numeros(numeros)
print("Números ordenados:", numeros_ordenados)