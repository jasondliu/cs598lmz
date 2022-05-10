import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
weakref.ref(lst[0],callback)
del a

import weakref
class A(object):pass
a=A()
b=A()
c=A()
a.c=b
b.c=a
a.b=c
b.a=a
c.a=b
c.b=a
del a
del b
del c

import weakref
class A(object):pass
a=A()
b=A()
c=A()
a.c=b
b.c=a
a.b=c
b.a=a
c.a=b
c.b=a
a.b=None
del a
del b
del c

import weakref
class A(object):pass
a=A()
b=A()
c=A()
a.c=b
b.c=a
a.b=c
b.a=a
c.a=b
c.b=a
c.a=None
del a
del b
del c

