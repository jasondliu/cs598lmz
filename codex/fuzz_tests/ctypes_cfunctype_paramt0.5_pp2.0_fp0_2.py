import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def py_func(x):
    return x**2

c_func = FUNTYPE(py_func)

print(c_func(2))
print(c_func(5))

# Функция с переменным числом аргументов
def py_func2(*args):
    return sum(args)

c_func2 = FUNTYPE(py_func2)

print(c_func2(2, 3, 5))
print(c_func2(2, 3, 5, 10))

# Функция с переменным числом аргументов
def py_func3(**kwargs):
    return sum(kwargs.values())

c_func3 = FUNTYPE(py_func3)

print(c_
