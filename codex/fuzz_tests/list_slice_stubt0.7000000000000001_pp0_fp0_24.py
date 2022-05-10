import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
del a,lst
gc.collect()
</code>
Python 2.7.3


A:

The reason for this is that the <code>gc</code> module implements a mark and sweep garbage collector.  If a cyclic reference is created, it will not be garbage collected.  In your case, you create a circular reference and then delete the reference to it.  However, the circular reference itself still exists and so <code>gc.collect()</code> will not free the memory.
If you change your code to the following, the object is removed:
<code>import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(
