import ctypes
# Test ctypes.CFUNCTYPE
LPrectangulo = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

@LPrectangulo
def rectangulo(a, b):
    print("\nHemos llamado a la funcion rectangulo")

    for i in range(1, b+1):
        for j in range(1, a+1):
            if i == 1 or i == b:
                print('#', end="")
            else:
                if j == 1 or j == a:
                    print('#', end="")
                else:
                    print(' ', end="")
        print()
rectangulo(4, 8)

print("Herencia")

class Libreria:
    def __init__(self, catego, titu, au):
        self.categoria = catego
        self.título = titu
        self.autor = au
        self.leidas = 0
    
