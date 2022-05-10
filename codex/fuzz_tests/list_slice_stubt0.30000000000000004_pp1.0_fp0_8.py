import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(a)
weakref.ref(lst[0],callback)
del a
del lst
import gc
gc.collect()
print keepalive
</code>

