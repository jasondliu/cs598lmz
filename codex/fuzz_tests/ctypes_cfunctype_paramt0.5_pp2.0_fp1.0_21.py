import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

c_f = FUNTYPE(f)

print(c_f(3))

# в качестве параметров функции можно передавать массивы
# и обрабатывать их в стиле С++

import numpy as np

a = np.array([1,2,3,4,5])

@np.vectorize
def f(x):
    return x**2

f(a)

# а можно использовать стандартный синтаксис для вектори
