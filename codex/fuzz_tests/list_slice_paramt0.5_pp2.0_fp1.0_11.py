import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
</code>
However, if I change the last line to <code>del a.c</code>, the list will be emptied.
Why is this?


A:

When you do <code>del a</code>, you are deleting the last reference to <code>a</code>. Since <code>a</code> is the only reference to <code>a.c</code>, <code>a.c</code> is also deleted.
When you do <code>del a.c</code>, you are deleting the reference to <code>a.c</code>, but <code>a</code> still exists.

