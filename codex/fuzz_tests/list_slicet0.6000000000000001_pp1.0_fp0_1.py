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

#coding:utf-8
import ctypes
import time
import weakref
def callback(x):
    del lst[0]
lst=[str()]
a=ctypes.c_void_p(id(lst[0]))
keepali0e=[]
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
