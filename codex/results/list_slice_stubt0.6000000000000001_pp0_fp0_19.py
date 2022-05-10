import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wref = weakref.ref(lst, callback)
del lst
import gc
gc.collect()
</code>
and here is the output:
<code>&gt;&gt;&gt; len(keepalive)
1
&gt;&gt;&gt; keepalive[0].c
&lt;__main__.A object at 0x0000000002B1D7F0&gt;
</code>
So this means that weakref.ref is not keeping a strong reference to the object it's referring to.
But if we change the code a little bit:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wref = weakref.ref(a, callback)
del lst
import gc
gc.collect()
</code>
and the output:
<code>&gt;&gt;&gt;
