import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepali0e.append(a)
keepali0e.append(a.d)
keepali0e.append(a.c)
del a.c
del a.d
del a
import os
gc.collect()
keepali0e[-1]=lst[0]
del lst
keepali0e[-2]=callback
del keepali0e
gc.collect()
print lst
