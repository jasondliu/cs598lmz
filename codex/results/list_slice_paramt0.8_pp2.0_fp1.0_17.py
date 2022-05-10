import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print len(lst)

import weakref
class A(object):pass
def callback(x):print "deleted"
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print keepali0e[0]()

import weakref
class A(object):pass
def callback(x):print "deleted"
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]()

import weakref
class A(object):pass
def callback(x):print "deleted"
keepali0e=[]
a=A()
a.c=a
print a.c,id(a.c)
keepali0e.append(weakref.ref(a.c,callback))
del a
print keepali0e[0]()

import weakref
class A(object):pass
def callback(x):print "
