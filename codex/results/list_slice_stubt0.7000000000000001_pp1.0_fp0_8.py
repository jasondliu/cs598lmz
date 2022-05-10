import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del keepalive[:]
gc.collect()
assert w() is None
assert not lst
import gc,weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del keepalive[:]
gc.collect()
assert w() is None
assert not lst
import gc,weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del keepalive[:]
gc.collect()
assert w() is None
assert not lst
import weakref,gc
class A(object):pass
def callback(x):raise Exception
a
