from types import FunctionType
a = (x for x in [1])
print(type(a))
def func():
    pass
print(type(func))
print(isinstance(func, FunctionType))

import os
print(os.path.abspath(os.path.join(os.getcwd(), '..')))

class A:
    def __init__(self):
        print('A')
class B(A):
    def __init__(self):
        super().__init__()
        print('B')
class C(A):
    def __init__(self):
        super().__init__()
        print('C')
class D(C, B):
    def __init__(self):
        super().__init__()
        print('D')
d = D()
print(D.__mro__)

# 实现一个无线的数值生成器
def my_range(start=0, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    while True
