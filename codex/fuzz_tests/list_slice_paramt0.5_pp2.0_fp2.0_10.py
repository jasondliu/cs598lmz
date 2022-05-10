import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

# the finalizer is called, and the weakref object is destroyed

# it is called when the object is destroyed, not when the weakref object is destroyed

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepalive=weakref.ref(a,callback)
del a

# the finalizer is called, but the weakref object is not destroyed

# it is called when the object is destroyed, not when the weakref object is destroyed

import weakref
class A(object):pass
def callback(x):print 'callback'
a=A()
a.c=a
keepalive=weakref.ref(a,callback)
del a
keepalive

# the finalizer is called, but the weakref object is not destroyed

# it is called when the object is destroyed, not when the weakref object is destroyed
