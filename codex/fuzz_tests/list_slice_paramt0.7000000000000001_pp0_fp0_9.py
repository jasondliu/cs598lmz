import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
del a
gc.collect()
lst

#(a)

import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
keepalive.append(weakref.ref(a,callback))
keepalive.append(weakref.ref(lst,callback))
del a
gc.collect()
lst

#(b)

import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
keepalive.append(weakref.ref(a,callback))
keepalive.append(weakref.ref(lst,callback))
a.c=a
del a
gc.collect()
lst

#(c)

import weakref
class A(object):pass
def callback(x):del lst[0]
keep
