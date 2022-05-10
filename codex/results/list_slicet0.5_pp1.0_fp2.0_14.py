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
print len(keepali0e)
</code>
This code will print <code>1</code>, not <code>2</code>.
But if I change the <code>callback</code> function to:
<code>def callback(x):del lst[0]
</code>
This code will print <code>2</code>.
I have read this document: https://docs.python.org/2/library/weakref.html#weakref.ref
But I still don't understand why.


A:

The reason for this behavior is that the <code>weakref.ref</code> object returned by <code>weakref.ref(a, callback)</code> is cyclic. The <code>weakref.ref</code> object maintains a reference to the object it is referencing, and the object maintains a reference to the <code>weakref.ref</code> object.
When the <code>weakref.ref</code> object is cyclic, the garbage collector will not destroy it, because it is reachable. So the callback will not be called.
To break the cycle, you could use <code
