import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
a.c.c=a
del a
keepali0e=[]
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=A()
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
a.c.c=a
del a
keepali0e=[]
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=[]
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
a.c.append(a)
del a
keepali0e=[]
import weakref
class A(object):pass
def callback(x):del lst
