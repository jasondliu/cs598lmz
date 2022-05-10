import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

del a
print len(lst)

import gc
gc.collect()
print len(lst)

import weakref
class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
w=weakref.ref(a,callback)
del w

del a
import gc
gc.collect()

import weakref
class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
w=weakref.ref(a,callback)
del a
import gc
gc.collect()

import weakref
class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
w=weakref.ref(a,callback)
del a
import gc
gc.collect()

import weakref
class A(object):pass
def callback(x):print "callback"
a=A()
a.c=a
w=weakref.ref(a,callback)
del a
