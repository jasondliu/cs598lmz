import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print('func', a, b)
    return a + b

f = FUNTYPE(func)

print(f(1, 2))

print('-' * 40)

import inspect

def func(a, b):
    print('func', a, b)
    return a + b

sig = inspect.signature(func)

print(sig)
print(sig.parameters)
print(sig.parameters['a'].kind)
print(sig.parameters['a'].default)
print(list(sig.parameters.values()))
print(list(sig.parameters.values())[0].name)
print(list(sig.parameters.values())[0].kind)

print('-' * 40)

import threading

def func(a, b):
    print(a, b)

func.is_running = False

def func(a, b
