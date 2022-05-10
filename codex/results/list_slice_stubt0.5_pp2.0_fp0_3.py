import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
del a
keepalive.append(lst)
del lst
keepalive.append(callback)
del callback
import gc
gc.collect()
for i in range(10):
    x=A()
    x.c=x
    keepalive.append(x)
    del x
    gc.collect()
    print len(gc.garbage)
