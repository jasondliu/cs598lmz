import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
</code>
I have tried to use <code>gc.collect()</code> to force garbage collection but it doesn't work.
Is there a way to force the garbage collection?
I'm using Python 3.2.3 on Ubuntu 12.04.1.


A:

There's no way to force the garbage collector to collect a given object. In fact, there's no way to force it to collect anything at all.
In CPython, you can force a full collection by calling <code>gc.collect()</code> with no arguments, but this is not guaranteed to collect everything.
In your case, though, it's not the garbage collector that's the problem. Your <code>callback</code> is being called, and it's deleting the reference to <code>a</code> from <code>lst</code>. But <code>a</code> still has a reference to itself in <code>a.c</code>, and <code>lst</code> still has a reference to <code>a</code> in <code>keepalive</code>. So, unless you delete <code>a.c</code>, <
