import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.__dict__=a
a.__weakref__=a
keepali0e.append(a)
del a

lst.append(weakref.ref(keepali0e[0], callback))
del lst
del keepali0e

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.__dict__=a
a.__weakref__=a
keepali0e.append(a)
del a
lst.append(weakref.ref(keepali0e[0], callback))
del lst
del keepali0e

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
