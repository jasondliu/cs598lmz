import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append(a)
del a
del keepalive
gc.collect()
</code>
It seems that if we define <code>__del__</code> in <code>A</code>, the <code>lst</code> and all other objects will be collected.
<code>In [1]: %paste
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append(a)
del a
del keepalive
gc.collect()
## -- End pasted text --
[None, None, None]


In [2]: %paste
import gc
import weakref
class A(object):
    def __del__(self):
        del lst[0]
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
