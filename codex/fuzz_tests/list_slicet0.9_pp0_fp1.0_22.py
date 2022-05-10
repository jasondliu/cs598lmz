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
lst.append(lst)


import dis
dis.dis(callback)

def callback(x):globals()[x]="What a surprise!"
keepali0e=[]
global globlst
globlst=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback,globlst[0]))
del a
import ctypes
allocator=ctypes.c_void_p
handles=[ctypes.c_void_p()]
capsule=allocator(id(1))
capsule
handles[0]

import dis
dis.dis(callback)

import sys
import ctypes
import weakref
capsule=ctypes.c_void_p()
mem=object()
capsule=ctypes.pointer(mem)

import dis
dis.dis(callback)

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keep
