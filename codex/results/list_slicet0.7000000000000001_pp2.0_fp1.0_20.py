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
The behavior is exactly the same as the <code>a.c=a</code> line is commented out. So why is the list not being deleted when the reference is broken?


A:

According to the documentation:
<blockquote>
<p>Callbacks are called as soon as <em>possible</em> after the referent is
  determined to be uncollectable, but no later than the next GC cycle.</p>
<p>The callbacks are called with a single argument, the weak reference
  object. If the callback function is None, the instance is deleted
  automatically.</p>
</blockquote>
The <code>weakref.ref</code> object is determined to be uncollectable, but the GC hasn't run yet. Your list is still holding a reference to the <code>weakref.ref</code> object.
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(
