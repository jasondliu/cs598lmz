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
It seems to work, but I'm not sure if it's 100% correct.


A:

Your <code>callback</code> function is the problem. It is modifying the list that the <code>lst</code> variable references, but the <code>weakref</code> module does not make any guarantees about what happens to the weak references in the list after the list itself is modified.
The <code>weakref</code> module documentation explicitly says this:
<blockquote>
<p>The contents of a weak reference list are not guaranteed to remain valid while the list is being iterated over. This is due to the fact that the list is internally implemented as an array of pointers, the contents of which may be modified by the garbage collector while the list is being iterated over. If you need to iterate over the list more than once, you should make a copy of the list and iterate over that instead.</p>
</blockquote>
So, even though you are not iterating over the list, the same problem can occur.

