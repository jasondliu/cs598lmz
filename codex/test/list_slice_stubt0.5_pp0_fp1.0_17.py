import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
keepalive=[]
keepalive.append(a)
keepalive.append(a.a)
keepalive.append(a.b)
keepalive.append(a.c)
del a
import gc
gc.collect()
