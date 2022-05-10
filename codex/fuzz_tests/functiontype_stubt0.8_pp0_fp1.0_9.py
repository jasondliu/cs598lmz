from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterable))

print('=============')

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def f():
    print('call f()')
fib(10)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
#print(f())
#print(f())
"""
"""
# 杨辉三角
# -*- coding: utf-8 -*-
def triangles():
    n = 0
    while True:
        n = n + 1
        L = [0]*n
        L[0], L[-1]
