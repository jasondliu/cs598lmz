import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]
del a
print keepali0e
import gc
gc.collect()
print keepali0e
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]
del a
print keepali0e
import gc
gc.collect()
print keepali0e
print keepali0e
print keepali0e
print keepali0e
import weakref
class A(object):pass
def callback(x):print x#del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]()
del a
print keepali0e
import gc
gc.collect()
print keepali0e
