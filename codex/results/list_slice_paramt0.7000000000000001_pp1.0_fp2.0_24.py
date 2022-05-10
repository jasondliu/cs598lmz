import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
d=lst[0]
import gc
for i in xrange(100):gc.collect()
len(d)

import weakref
class A(object):
    pass
class B(object):
    pass
def callback(a,b):
    print 'callback'
    b.append(1)
a=A()
a.c=a
b=B()
lst=[]
keepalive=[]
keepalive.append(weakref.ref(a,partial(callback,b=lst)))
del a
del b
import gc
gc.collect()
lst

from functools import partial
from weakref import ref
class A(object):
    pass
class B(object):
    pass
a=A()
b=B()
a.b=b
b.a=a

def c(b):
    print 'c'
keepalive=[]
keepalive.append(ref(a,partial(c,b)))
del a
del b
import gc
gc.collect()
