import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst
import gc
gc.collect()
print lst

class A(object):
    def __init__(self):
        self.b=B(self)
    def __del__(self):
        print 'del A'
class B(object):
    def __init__(self,a):
        self.a=a
    def __del__(self):
        print 'del B'
a=A()
del a

import weakref
class A(object):pass
def callback(x):print 'callback'
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
import gc
gc.collect()

import weakref
class A(object):pass
def callback(x):print 'callback'
keepali0e=[]
a=A()
