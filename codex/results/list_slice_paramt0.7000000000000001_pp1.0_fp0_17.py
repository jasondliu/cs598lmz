import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
a=None
del keepali0e
gc.collect()
</code>
It works well on Python 3.3.3, but on Python 2.7.3, it doesn't work.


A:

You're violating the Weak Reference Lifecycle:
<blockquote>
<p>The callback is called at some point after the referenced object dies, unless another cycle involving it is discovered first. Such cycles are common and unpredictable, and the module does not clean them up automatically.</p>
</blockquote>
In this case, <code>a</code> dies and there's a cycle involving it.  The callback is never called.  To fix this problem, you must break the cycle by <code>del a.c</code> after <code>a=None</code>.

