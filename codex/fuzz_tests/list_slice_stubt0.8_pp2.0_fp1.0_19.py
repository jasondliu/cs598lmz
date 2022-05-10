import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
keepali0e.append(a)
del a
lst.append(0xdeadbeef)
print(lst)
'''
from __future__ import print_function
import gc
import weakref
from string import ascii_letters
from random import randint
from sys import getrefcount
from ctypes import py_object
from ctypes import c_void_p
class A(object):pass
def tortury(start_at=None,max_dead=100,max_steps=100,keep_max_size=100,max_size=100000):
    gc.collect()
    dead=[]
    objects=[]
    print("\nStarting at:",start_at)
    start_at=start_at or dict((x,x) for x in range(100))
    lst=[start_at]
    for step in range(max_steps):
        if step%100==0:
            print("\rStep %d."%step,end='')
        if step
