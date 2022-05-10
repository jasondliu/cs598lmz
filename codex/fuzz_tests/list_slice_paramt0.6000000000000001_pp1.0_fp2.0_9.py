import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del lst
import gc
gc.collect()
del gc
</code>
What happens here is that the callback is only called once when the last reference to the object is deleted, but I would expect it to be called three times, once for each reference.
Why is this happening?


A:

<code>a.c</code> is a circular reference, so the object <code>a</code> will never be garbage collected. The <code>weakref</code> callback is only called when the object is garbage collected.

