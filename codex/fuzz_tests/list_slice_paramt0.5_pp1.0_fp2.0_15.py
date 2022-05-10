import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
del a
del lst
import gc
gc.collect()
</code>
According to the documentation, the <code>callback</code> function should be called. However, it is not.
Is this a bug in Python, or am I doing something wrong?
I am using Python 2.7.6.


A:

The problem is the circular reference. Once <code>a</code> is deleted, the reference count on <code>a.c</code> drops to 1, and it's not cleared.
The documentation states:
<blockquote>
<p>The callback is called as callback(ref) where ref is the proxy being finalized.</p>
</blockquote>
In this case, the proxy is <code>a</code>, and the reference count on <code>a</code> is 0, so the callback is called.

