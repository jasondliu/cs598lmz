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
The list of <code>str()</code> objects is never empty.
I've tried to add <code>gc.collect()</code> and <code>time.sleep(0.1)</code> but it doesn't help.
Edit:
I've tried to run the code on different computers and it works as expected. On my computer it doesn't.
I'm using Python 2.7.3 and Ubuntu 12.10.


A:

I think the problem is that you are using <code>weakref.ref</code> incorrectly.  You must pass a callable to the <code>ref</code> constructor, not a callable and a callback.  The callable is the thing to be weakly referenced, and the callback is the thing to be called when the reference dies.  So you need to do:
<code>lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
</code>
and then remove the <code>callback</code> parameter from the call to <code>weakref.
