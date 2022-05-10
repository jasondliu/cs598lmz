import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
keepali0e.append(lst)
del a
import gc
gc.collect()
print lst
print len(lst)
print keepali0e
print len(keepali0e)
