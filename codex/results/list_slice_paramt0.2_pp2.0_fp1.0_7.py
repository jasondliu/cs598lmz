import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

print '-'*20

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e

print '-'*20

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e

print '-'*20

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print keepali0e

print '-'*20

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepali0e=weakref.ref(a
