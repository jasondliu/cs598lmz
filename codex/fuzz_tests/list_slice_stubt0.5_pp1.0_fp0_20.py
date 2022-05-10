import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
a.c.d=a.c
keepali0e.append(a.c.d)
del a
del a.c
del a.c.d
lst[0]=a
a=None
lst[0]=a.c
a.c=None
lst[0]=a.c.d
a.c.d=None
del keepali0e
lst[0]=None
lst=None
import gc
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc
