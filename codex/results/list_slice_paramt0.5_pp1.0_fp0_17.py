import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
lst=[]
print(lst)

import weakref
class A(object):pass
def callback(x):print("callback called with x=",x)
a=A()
a.c=a
weakref.ref(a,callback)
del a

import weakref
class A(object):pass
def callback(x):print("callback called with x=",x)
a=A()
a.c=a
weakref.ref(a,callback)
del a

import weakref
class A(object):pass
def callback(x):print("callback called with x=",x)
a=A()
a.c=a
weakref.ref(a,callback)
a=None

import weakref
class A(object):pass
def callback(x):print("callback called with x=",x)
a=A()
a.c=a
weakref.ref(a,callback)
a=None

import weakref
class A(object):pass
def callback(x):print("callback
