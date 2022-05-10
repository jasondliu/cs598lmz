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

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
r=weakref.ref(a,callback)
del a
print r()
print r()

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
r=weakref.ref(a,callback)
del a
print r()
print r()

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
r=weakref.ref(a,callback)
del a
print r()
print r()

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
r=weakref.ref(a,callback)
del a
print r()
print r()

import weakref
class A(object):pass
def callback(x):print '
