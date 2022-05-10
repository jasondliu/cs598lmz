import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.x=a
del a.c
keepalive=[a]
lst.append(a)
a=None
print lst
del lst
print keepalive
print keepalie
del keepali0e
del keepalive
import gc
print gc.collect()
