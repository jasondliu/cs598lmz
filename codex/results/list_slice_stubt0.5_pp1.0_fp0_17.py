import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
del a
gc.collect()
keepalive=[]
del keepalive
gc.collect()
del lst
gc.collect()
</code>
I have checked the <code>gc.garbage</code> and it is empty. I have also checked the <code>gc.get_referrers(callback)</code> and <code>gc.get_referrers(lst)</code> and they are empty.
What I am doing wrong and how to get rid of this memory leak?


A:

The problem is that the weak reference is not cleared.
You need to clear it yourself.
<code>import gc
import weakref

class A(object):pass

def callback(x):
    del lst[0]
    del ref

keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
ref = weakref.ref(a, callback)
del a
gc.collect()
keepalive=[]
del keepalive
gc.collect()
del l
