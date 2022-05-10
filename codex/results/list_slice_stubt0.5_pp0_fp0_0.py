import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a,callback)
print(wr)

del a
print(wr)
print(lst)

import weakref
class A(object):pass
def callback(x):print('callback',x)
a=A()
wr=weakref.ref(a,callback)
print(wr)
del a
print(wr)

import weakref
class A(object):pass
def callback(x):print('callback',x)
a=A()
wr=weakref.ref(a,callback)
print(wr)
a=None
print(wr)

import weakref
class A(object):pass
def callback(x):print('callback',x)
a=A()
wr=weakref.ref(a,callback)
print(wr)
a=None
print(wr)

import weakref
class A(object):pass
def callback(x):print('callback',x)
a=A()
wr=weakref.ref(a,callback)
print(wr)
a=None
