import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(lst[0],callback))
lst.append(weakref.ref(lst[0],callback))
del lst
import gc
gc.collect()

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print(keepalive[0].c)

print
