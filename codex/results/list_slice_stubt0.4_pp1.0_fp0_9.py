import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
lst.append(str())
del a
del lst[:]
gc.collect()
print keepali0e[0]()

import weakref
class A(object):pass
def callback(x):print 'callback'
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print keepali0e[0]()

import weakref
class A(object):pass
def callback(x):print 'callback'
keepali0e=[]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print keepali0e[0]()

import weakref
class A(object):pass
def callback(x):print 'callback'
keepali0e=[]
a=A()
a.c=a
keepali0e.append(
