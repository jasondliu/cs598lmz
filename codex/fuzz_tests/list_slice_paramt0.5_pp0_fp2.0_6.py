import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=a
del a
del keepali0e
import gc
gc.collect()
print lst[0]
print len(gc.garbage)
