import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(lst)
del lst
print(keepali0e)

import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(keepali0e)

import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(keepali0e)

import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(keepali0e)

import weakref
class A(object):pass
def callback(x):
