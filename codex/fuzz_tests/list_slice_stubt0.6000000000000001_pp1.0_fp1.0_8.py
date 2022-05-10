import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(A(),callback)
del lst
keepalive[0].c=None
</code>
The reference count of <code>A</code> is 0 and <code>del lst[0]</code> has been called, but <code>A</code> is still in memory.
Why?


A:

You've created a <code>weakref.ref</code> to <code>A</code>. That's not a reference to <code>A</code>, it's a reference to a weak reference object. The <code>A</code> object is not referenced in any way from anywhere.

