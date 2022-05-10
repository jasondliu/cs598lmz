import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.lst=lst
a.keepali0e=keepali0e
a.keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
import gc
gc.collect()
print len(lst)
