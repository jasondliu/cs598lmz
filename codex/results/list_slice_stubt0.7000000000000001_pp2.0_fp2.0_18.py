import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
print(hex(id(a.b)))
print(hex(id(a.c)))
a.b.b=a.b
a.b.b=a.c
print(hex(id(a.b.b)))
print(hex(id(a.c)))


'''
import traceback
import inspect
import threading
import time
import sys
import gc
class A:
    def __init__(self):
        pass
    def __del__(self):
        print("__del__",self)
        self.b=self
        gc.collect()
        print("__del__",self)

def a():
    a=A()
    a.b=a
    print("a",a)
    del a
    gc.collect()
    print("a",a)
    return

a()
'''
