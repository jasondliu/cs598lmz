import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
lst[0]=weakref.ref(a,callback)
del a
for i in xrange(100):
    lst.append(str())
    lst[-1]=weakref.ref(a,callback)
    del a
    a=A()
    a.c=a
    keepalive=a
    keepalive=lst
lst=None
keepalive=None
import gc
gc.collect();gc.collect();gc.collect()
print "OK"
