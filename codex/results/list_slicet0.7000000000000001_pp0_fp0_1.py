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
Is that right?
Thanks.


A:

The reference cycle is a cycle of strong references.  So long as the cycle has a strong reference in it somewhere, the objects will not be destroyed and the memory will not be released.
A <code>weakref</code> is not a strong reference.  It is a weak reference.  It will not keep the object alive.
Therefore, it is not possible to create a <code>weakref</code> cycle.  Adding a <code>weakref</code> to the cycle will not keep the objects alive.  Thus, it will not prevent the objects from being destroyed and the memory from being released.

