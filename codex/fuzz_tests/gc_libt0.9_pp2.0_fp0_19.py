import gc, weakref

class MyClass:
    a = 1
    b = 2

class Addr:
    def __init__(self, addr):
        self.addr=addr
    def __repr__(self):
        return hex(self.addr)

def get_addr(x):
    return Addr(id(x))

def dump(obj):
    print('ADDR:', get_addr(obj), type(obj), sep='    ')
    if isinstance(obj, MyClass):
        for attr in ('a', 'b'):
            print(attr, '=', getattr(obj, attr))
    elif hasattr(obj, '__dict__'):
        for attr in obj.__dict__:
            print(attr, '=', getattr(obj, attr))
    print()

import sys

X = MyClass()
Y = MyClass()
Z = MyClass()

print('BEFORE:')
dump(X)
dump(Y)
dump(Z)

def kill_obj(obj):
    obj
