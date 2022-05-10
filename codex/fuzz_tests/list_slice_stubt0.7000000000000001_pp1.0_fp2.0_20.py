import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepali0e.append(a)
lst.append(weakref.ref(str(),callback))
keepali0e.append(a)
keepali0e.append(a)
del keepali0e
gc.collect()
import weakref
class A(object):pass
def callback(x):del lst[0]
a=A()
a.c=a
a.b=a
a.a=a
del a
lst=[str()]
lst.append(weakref.ref(str(),callback))
del lst
gc.collect()
import weakref
class A(object):pass
def callback(x):del lst[0]
a=A()
a.c=a
a.b=a
a.a=a
del a
lst=[str()]
lst.append(weakref.ref(str(),callback))
del lst
gc.collect()
