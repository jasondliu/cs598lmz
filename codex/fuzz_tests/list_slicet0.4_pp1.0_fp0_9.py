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
print(keepali0e)
</code>
I want to know why the output is <code>[[&lt;weakref at 0x7f8a8a3c3e18; to 'A' at 0x7f8a8a3c3d68&gt;], []]</code> instead of <code>[[&lt;weakref at 0x7f8a8a3c3e18; dead&gt;], []]</code>?
I know that the reference count of <code>a</code> is 2 because of <code>a.c=a</code>. But why the reference count of <code>a</code> is still 2 after deleting <code>a</code>?


A:

When you delete <code>a</code>, you are only deleting the local reference to <code>a</code>.  The reference to <code>a</code> in <code>keepalive</code> is still there, and so <code>a</code> is still alive.  When you delete the reference to <code>a</code> in <code>keepalive
