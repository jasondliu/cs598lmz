import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
print weakref.getweakrefcount(a)
del a
print lst
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=[]
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
print weakref.getweakrefcount(a)
del a
print lst
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
print weakref.getweakrefcount(a)
del a
print lst
import weakref
class A(object):pass
def callback(x):del l
