import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del a.c
assert lst==[]

import weakref
class A(object):pass
class B(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
b=B()
a.c=b
b.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(b,callback))
keepali0e.append(weakref.ref(b.c,callback))
del a
del a.c
del b
del b.c
assert lst==[]

import weakref
class A(object):pass
class B(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
b=B()
a
