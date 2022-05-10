import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
</code>
This code raises an exception: <code>TypeError: __delete__ takes exactly 2 arguments (1 given)</code>, but when I make little change:
<code>lst=[None]
</code>
then the same code does not raise any errors.
So, why does the (1 given) error occurs?
Btw, I use Python 2.5.4


A:

I could reproduce the problem under 2.7.3, though not under 2.7.13. Looks like a bug, but I haven't investigated further.
The problem seems to be based on the fact that <code>callback</code> doesn't actually need to be called.  <code>del lst[0]</code> removes the reference <code>lst[0]</code> (pointing to the empty string) to this list, which has no impact.
I don't understand why you need <code>str()</code> in <code>lst</code> either, or why you need <code>a.c = a</code> at all, since it's the only reference to the
