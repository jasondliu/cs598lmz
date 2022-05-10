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
Is there some way to make the callback to be called?
Update:
When I tried to run the callback manually, I discovered that it seems to be a bug.
Here is a bug report.


A:

From the docs on <code>weakref.WeakSet</code>:
<blockquote>
<p>In addition, a weak reference to the object is made, the strong reference to the object is removed, and then the object’s <code>&lt;code&gt;__del__()&lt;/code&gt;</code> method, if any, is called.</p>
</blockquote>
Now, I am not sure if you asked the wrong question or if I understood it wrong, but from your example it seems like you are expecting a callback to be called when an object is garbage collected. This is not what the callback is for. The callback is for when the object is removed from the weak set.

