import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=A()
a.b.a=a
a.b.b=a.b
a.b.c=a
keepalive.append(a)
keepalive.append(a.b)
del a
del a.b
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a.b,callback))
del lst
import gc
gc.collect()
print(lst)
print(keepalive)
print(callback)
