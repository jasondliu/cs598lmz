import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(weakref.ref(a.c,callback))

print lst
del a
print lst

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(weakref.ref(a,callback))

print lst
del a
print lst

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(weakref.ref(a.c.c,callback))

print lst
del a
print lst

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst
