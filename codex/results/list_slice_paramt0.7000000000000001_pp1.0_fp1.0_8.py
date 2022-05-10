import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
print(lst)

#可以看到str还在

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
print(lst)
