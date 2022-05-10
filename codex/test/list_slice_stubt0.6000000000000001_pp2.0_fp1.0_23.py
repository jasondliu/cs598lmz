import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
print(lst,keepali0e)
del a
del lst
print(keepali0e)

import weakref
class A(object):pass
def callback(x):print('callback',a)
a=A()
keepali0e=weakref.ref(a,callback)
print(keepali0e)
del a
print(keepali0e)

import weakref
class A(object):pass
def callback(x):print('callback',a)
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
print(keepali0e)
del a
print(keepali0e)

import weakref
class A(object):pass
def callback(x):print('callback',a)
a=A()
b=A()
c=A()
a.b=b
a.c=c
b.c=c
keepali0e=weakref.ref(a,callback)
