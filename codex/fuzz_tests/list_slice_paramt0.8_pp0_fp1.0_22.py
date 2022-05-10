import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
a.callback=callback
del a
import gc
gc.collect()
keepali0e[0]()
keepali0e[1]()
