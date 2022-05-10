import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(x, y):
    return x + y

f_c = FUNTYPE(f)

print(f_c(1, 2))

# Пример вызова функции из библиотеки

import ctypes

# Загрузка библиотеки
lib = ctypes.CDLL('./lib.so')

# Описание функции из библиотеки
lib.f.argtypes = [ctypes.c_int, ctypes.c_int]
lib.f.restype = ctypes.c_int

# Вызов функции из библ
