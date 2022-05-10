import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
</code>
However, I see no effect of <code>callback</code> being called when I test this (using Python 3.5).  The <code>keepali0e</code> list is empty after the <code>a</code> object is garbage-collected, but <code>del lst[0]</code> is never executed.  (I would have expected this to execute straight away, since <code>a</code> is no longer a strong reference to <code>a.c</code> once it is assigned to <code>keepali0e</code>, but even if that's not the case, I would expect it to execute once <code>a</code> is garbage-collected.)
I thought perhaps this was something about the <code>str</code> object that is being referenced by the weakref, but I'm pretty sure the same thing happens with other objects (I'm not sure how to test it, though).
Is there something I'm missing about this?  Is this a bug?


A:

Your code works for me in Python 2.7.10 and 3.5.
