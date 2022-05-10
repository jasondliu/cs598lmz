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
print(len(keepali0e))
</code>
The problem is that the weakref callback is never called. I am using Python 3.3.3.


A:

You're creating a cyclic reference, which is not supported by weakrefs.  From the weakref docs:
<blockquote>
<p>Weak references to objects are not kept alive solely by the existence of a reference to the object from the weak reference object. Rather, they exist only while there is at least one strong reference to the object. When the last strong reference to an object is deleted, it is immediately eligible for garbage collection and any weak references to it will be dead.</p>
</blockquote>
In your code, you create a cyclic reference with <code>a.c = a</code>, so there is always a strong reference to <code>a</code> and the weakref callback is never called.  If you remove the <code>a.c = a</code> line, the callback is called as expected.

