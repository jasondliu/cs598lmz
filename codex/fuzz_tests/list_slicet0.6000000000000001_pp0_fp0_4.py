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
In the OP's code, a cyclic reference is created by <code>a.c=a</code>, and then <code>a</code> is deleted.  This is intended to cause the callback to be called, deleting the first element of <code>lst</code>.  This will break the loop, letting the code terminate.
However, the loop is never broken.  After the <code>del a</code>, <code>lst[0]</code> is still a <code>str</code>, not a <code>weakref</code>, and <code>lst[0]</code> is not a reference to <code>a</code>.  Thus, the callback is never called.
To get the callback to be called, one has to switch out <code>lst[0]</code> for a <code>weakref</code> that references <code>a</code>.  This can be done by using the second argument to <code>weakref.ref</code> as follows:
<code>def callback(x):del lst[0]
lst=[str()]
a=
