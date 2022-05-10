import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("** MUTIPLICACION DE MATRICES **")
columnas = int(input("Digite la cantidad de columnas: "))
filas = int(input("Digite la cantidad de filas: "))

matrizA = []
matrizB = []
matrizC = []

for i in range(filas):
    matrizA.append([0]*columnas)
    matrizB.append([0]*columnas)

for i in range(filas):
    matrizC.append([0]*columnas)

for i in range(filas):
    for j in range(columnas):
      matrizA[i][j] = int(input("Digite un numero para la primera matriz en la posicion fila/columna : "))

print("\n")

for i in range(filas):
    for j in range(columnas):
      matrizB[i][j] = int(input("Digite un numero para la primera se
