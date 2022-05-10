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
I don't understand how the reference counter for a gets to 0, in other words when does the reference count for a created by the <code>a=A()</code> line decrease, and when does it increase?


A:

<code>a.c=a
</code>
At this point, the reference count of <code>a</code> is 1, because <code>a.c</code> references <code>a</code>. 
<code>keepali0e.append(weakref.ref(a,callback))
</code>
At this point, the reference count of <code>a</code> is 2, because <code>keepali0e</code> references <code>a</code> through the newly created <code>weakref</code> object. (The <code>weakref</code> object doesn't increase the reference count of <code>a</code>.)
<code>lst[0] = ''
</code>
At this point, the reference count of <code>a</code> is 1 again, because the <code>weakref</code> object
