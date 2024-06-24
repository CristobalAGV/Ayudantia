matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def sumar_matriz(matriz):
    suma=0
    for fila in matriz:
        for elemnto in fila:
            suma += elemnto
    return suma

def transponer_matriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    matriz_transpuesta=[]
    for c in range(columnas):
        nueva_fila=[]
        for f in range(filas):
            nueva_fila.append(matriz[f][c])
        matriz_transpuesta.append(nueva_fila)
    return matriz_transpuesta

print(f"Suma de todas las celdas de la matriz: {sumar_matriz(matriz)}")

print(f"Matriz transpuesta: ")
for fila in transponer_matriz(matriz):
    print(fila)