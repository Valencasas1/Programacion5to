def crear_matriz():
    matriz= []
    for i in range (4):
        fila = []
        for j in range(4):
            valor= float(input(f"ingrese el valor para la posicion({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz
def suma_diagonal(matriz):
    suma=0
    for i in range(4):
        suma += matriz[i][i]
    return suma
def multiplicacion_diagonal(matriz):
    producto = 	1
    for i in range(4):
        producto *= matriz[i][i]
    return producto
mi_matriz = crear_matriz()
suma_diagonal_principal= suma_diagonal(mi_matriz)
print(f"la suma de la diagonal principal es: {suma_diagonal_principal}")
multiplicacion_diagonal_principal = multiplicacion_diagonal(mi_matriz)
print(f"la multiplicacion de la diagonal principal es: {multiplicacion_diagonal_principal}")
    
    
        