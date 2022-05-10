import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
a=lst[0]
print(a)
print(w())

import weakref
class A(object):pass
def callback(x):print(x)
keepalive=[]
a=A()
b=A()
a.b=b
b.a=a
keepalive.append(a)
keepalive.append(b)
w=weakref.ref(a,callback)
del a
del b
print(w())

import weakref
class A(object):pass
def callback(x):print(x)
keepalive=[]
a=A()
b=A()
a.b=b
b.a=a
keepalive.append(a)
keepalive.append(b)
w=weakref.ref(a,callback)
del a
print(w())

import weakref
class A(object):pass
def callback(x):print(x)
keepalive=[]
a=A()

