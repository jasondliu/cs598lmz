import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
callback(a)

import weakref
class A(object):
    __slots__=("foo","__weakref__")
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.foo=a
keepali0e.append(weakref.ref(a))
callback(a)

import weakref
class A(object):
    __slots__=("foo","__weakref__")
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.foo=a
keepali0e.append(weakref.ref(a))
callback(a)

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a.__dict__))
def g():
    a.c=a
callback(a)
g()

