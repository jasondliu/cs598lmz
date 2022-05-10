import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(keepalive)
keepalive.append(a)
wr=weakref.ref(a,callback)
print(wr)
print(len(lst))
print(lst)
del keepalive
del a
import gc
gc.collect()
print(len(lst))
print(lst)
print(wr)
del wr
