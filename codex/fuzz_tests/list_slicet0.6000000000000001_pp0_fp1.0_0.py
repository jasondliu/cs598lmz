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
print keepali0e
</code>
I want to know is there any way to get the reference to <code>a</code> or <code>a.c</code> in the list <code>keepali0e</code>? I know that the object <code>a</code> is located in the second place in the list <code>keepali0e</code>.
I tried to use <code>gc.get_referrers(a)</code> to get the reference to <code>a</code>. But I failed.


A:

The problem is the <code>a.c=a</code> creates a circular reference.  So when the reference count for <code>a</code> drops to 0, it does not get deleted because the reference to <code>a</code> in <code>a.c</code> keeps it alive.  The reference count for <code>a</code> drops to 0 when you do the <code>del a</code>.
If you add a <code>del a.c</code> before the <code>del a</code>, it will delete <code>a
