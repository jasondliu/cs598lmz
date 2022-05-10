import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
keepalive.append(callback)
del a
lst[0].c=lst
del lst
import gc
gc.collect()
while keepalive:pass
</code>

