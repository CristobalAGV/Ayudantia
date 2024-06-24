matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def escribir_matriz_archivo(matriz, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:   
        for fila in matriz:
            archivo.write(''.join(map(str, fila))+"\n")

def leer_matriz_archivo(matriz, nombre_archivo):
    matriz=[]
    with open(nombre_archivo,"r") as archivo:
        for linea in archivo:
            fila=list(map(int, linea.split()))
            matriz.append(fila)
    return matriz

nombre_archivo="matriz.txt"