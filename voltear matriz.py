matriz = [[1, 2, 3, 4, 5, 6],
          [7, 8, 9, 10, 11, 12],
          [13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29, 30],
          [31, 32, 33, 34, 35, 36]]
def voltear_m(matriz):
    return[fila[::-1]for fila in matriz]

print("matriz original: ")
for fila in matriz:
    print (fila)
    
matriz_volteada = voltear_m(matriz)
print("Matriz volteada horizontalmente")
for fila in matriz_volteada:
    print(fila)