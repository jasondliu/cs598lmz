import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(lst)
del a
print(lst)
del lst[0]
print(lst)

import weakref
class A(object):pass
def callback(x):print('callback',x)
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(lst)
del a
print(lst)
del lst[0]
print(lst)

import weakref
class A(object):pass
def callback(x):print('callback',x)
keepalive=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
print(lst)
del a
print(lst)
del lst[0]
print(lst)

import weakref
class A(object):pass
def callback(x):print
