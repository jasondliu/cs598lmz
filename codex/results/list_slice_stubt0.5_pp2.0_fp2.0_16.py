import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
lst.append(weakref.ref(lst,callback))
del lst
del keepali0e
import gc
gc.collect()
gc.collect()
gc.collect()
gc.collect()
