import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(weakref.ref(a,callback))
lst.append(lst)
keepali0e.append(lst)
del a
del lst
import gc
gc.collect()
