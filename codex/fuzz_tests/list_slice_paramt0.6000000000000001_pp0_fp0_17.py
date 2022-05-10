import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst

print '-'*20

import weakref
class A(object):pass
def callback(x):print x
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]()
del a
print keepali0e[0]()

print '-'*20

import weakref
class A(object):pass
def callback(x):print x
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]()
del a
print keepali0e[0]()

print '-'*20

import weakref
class A(object):pass
def callback(x):print x
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0
