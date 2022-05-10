import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
</code>
The problem is that the callback is not called when the list is cleared.
If I change the line <code>a.b=weakref.ref(a,callback)</code> to <code>a.b=weakref.ref(a)</code> it works.


A:

I think the problem is that the list is not being cleared.
<code>del lst[0]</code> doesn't remove the first element from the list, it removes the first element from the list.  In your example, <code>lst</code> is still a list containing a single element, which is a reference to the empty string.
The callback will be called if you do <code>lst.pop(0)</code> or <code>lst.remove(str())</code> or <code>lst[:] = []</code>.

