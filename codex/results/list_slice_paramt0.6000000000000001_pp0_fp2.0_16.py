import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
a=None
lst[0]='foo'
del lst
</code>
I have tried the above code. But the callback function is not called. But if I use <code>keepalive=keepali0e</code>, it works.
The first question is why?
The second question is how to use <code>keepalive</code> to keep the reference(a) alive?


A:

The documentation says
<blockquote>
<p>The optional callback is called with a single argument, the weakref object, and is usually used to remove the weakref from an internal list.</p>
</blockquote>
So the callback should be called when the weakref object is deleted, not when the object it references is deleted.  In your example, the weakref object is deleted when you execute <code>del lst[0]</code>, so that's when you should expect the callback to be called.
If you want the callback to be called when the object is deleted, you need to create a second weakref object
