import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print 'before del a: ',lst[0]
del a
print 'before gc: ',lst[0]
import gc
gc.collect()
print 'after  gc: ',lst[0]
