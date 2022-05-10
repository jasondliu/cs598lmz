import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
weakref.ref(lst[0],callback)
del keepali0e
del lst
import gc
gc.collect()
</code>
I get
<code>gc: invalid object in weakref table
</code>
But if I delete line 9, I don't get the error.
Why is this?

