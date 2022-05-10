import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

import gc
gc.collect()
print lst

import weakref
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
del a
del b
print gc.collect()
import weakref
class A(object):
    def __init__(self):
        self.b=A()
a=A()
del a
print gc.collect()

import weakref
class A(object):
    def __init__(self):
        self.b=A()
a=A()
del a
print gc.collect()

import weakref
class A(object):
    def __init__(self):
        self.b=A()
a=A()
del a
print gc.collect()

import weakref
class A(object):
    def __init__(self):
        self.b=A()
a=A()
del a
print gc.collect()

import weakref
class A(object):

