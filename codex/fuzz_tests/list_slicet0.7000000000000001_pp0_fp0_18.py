import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
"""

class A(object):pass

def callback(x):
    del lst[0]

keepali0e = []

lst = [str()]
a = A()
a.c = a
keepali0e.append(weakref.ref(a, callback))
del a
while lst:
    keepali0e.append(lst[:])

import gc
gc.collect()

import ctypes

class A(object):
    pass
def callback(x):
    del lst[0]
keepali0e=[]
lst=[A()]
keepali0e.append(weakref.ref(lst[0],callback))
del lst[0]
while lst:keepali0e.append(lst[:])

"""

class A(object):
    pass

def callback(x):
    del lst[0]

keepali0e = []

lst = [A()]
keepali0e.append(weakref.ref(lst[0], callback))

