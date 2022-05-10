import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
keepalive.append(lst)
del a
del lst
import gc
gc.collect()
for o in gc.get_objects():
    if isinstance(o,A):
        print o
        o.c=None
        print o
        o.c=o
        print o
        o.c=None
        print o
        o.c=o
        print o
        o.c=None
        print o
        o.c=o
        print o
        o.c=None
        print o
        o.c=o
        print o
        o.c=None
        print o
        o.c=o
        print o
        o.c=None
        print o
        o.c=o
        print o
        o.c=None
        print o
        o.c=o
        print o
        o.c=None
        print o
        o.c=o
        print o
        o.c=None
        print o
