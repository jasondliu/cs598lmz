import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[]
lst.append(a)
keepalive.append(weakref.ref(lst,callback))
del a#lst[0]
del keepalive[0]

import gc
gc.collect()

import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(lst,callback))
del a
del keepalive[0]

import gc
gc.collect()

import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(lst,callback))
del a
del keepalive[0]

import gc
gc.collect()

import weakref
class A(object):pass
def callback(x):del lst[0]

