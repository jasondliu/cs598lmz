import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
a.b=lst
lst.append(a)
keepalive=lst
del lst
keepalive.append(callback)

import gc
gc.collect()

class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
a.b=lst
lst.append(a)
keepalive=lst
del lst
keepalive.append(callback)

import gc
gc.collect()

class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
a.b=lst
lst.append(a)
keepalive=lst
del lst
keepalive.append(callback)

import gc
gc.collect()

class A(object):pass
