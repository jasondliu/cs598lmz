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
The above code is taken from the link. Any ideas why this is happening?


A:

To answer the question directly, the <code>keepalive</code> list is populated by references to the <code>str</code> objects that are in <code>lst</code> at the time you append it. If the <code>str</code>s in <code>lst</code> get garbage collected, the <code>str</code>s in <code>keepalive</code> will be garbage collected too, and <code>keepalive</code> will be empty.
I'm not sure what the point of this code is. It seems to be trying to demonstrate that the <code>callback</code> function is not called when the <code>A</code> object is garbage collected. It's been explained that this is because <code>A</code> is a classic class and not a new-style class, but even if it were a new-style class it would still be impossible to prove that the callback is called, since the callback itself deletes the reference to <code>a</code>.
If you modify
