import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(lst))
keepali0e.append(weakref.ref(lst[0]))
keepali0e.append(weakref.ref(callback))
keepali0e.append(weakref.finalize(a,callback,lst))
import gc
gc.collect()
print(keepali0e[-1]())
