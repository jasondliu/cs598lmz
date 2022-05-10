import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int)

# Funciones
def func(x,y):
    return x[0] + y[0]

def func2(x,y,z):
    return x[0] + y[0] + z

# Instancia de la funcion
f = FUNTYPE(func)
f2 = FUNTYPE2(func2)

# Variables
a = ctypes.c_int(1)
b = ctypes.c_int(2)
c = ctypes.c_int(3)

# Puntero a variables
pa = ctypes.pointer(a)
pb = ctypes.pointer(b)
pc = ctypes.pointer(c)

# Llamada a
