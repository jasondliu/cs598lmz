import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
a.x=weakref.ref(a,callback)
</code>
The code creates a cyclic reference between itself and a weak reference to itself.  When the weak reference goes away, it should delete one of the strings in <code>lst</code>.  Since <code>lst</code> is in a cyclic reference with <code>a</code>, it should not be garbage collected, and thus the <code>str()</code> object should not be garbage collected.
However, this is the output I get:
<code>&gt;&gt;&gt; gc.collect()
0
&gt;&gt;&gt; gc.collect(2)
0
</code>
Trying with Python 2.7.1, I get the same results.  What's going on?


A:

This is because the <code>weakref</code> object is a proxy object.  It is not part of the cycle.  And it is not visible in the <code>__dict__</code> of the
