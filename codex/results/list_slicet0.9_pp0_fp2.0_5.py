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
But it looks rather ugly, and above all, it is not fast.
Since the GC will never be in this state when there is a user of the application, I am not too worried about the fact that this will not work on every Python.

Notes:

It is not possible to put the global variable anywhere else that I know of.
It is not possible to put the call to <code>keepalive</code> anywhere else.
It is not possible to not have the <code>keepalive</code> variable, even though it does nothing.
It is not possible to put the keepalive in the list start up.
It is not possible to use <code>id</code>, because that does not work across C encapsulation boundaries (like file IO).
It is not possible to use <code>__hash__</code>, because that is not implemented for all Python types.
It is not possible to use something else than a list.
It is not possible to use a built-in type, because they are considered immutable (<code>list</code> is not).



A:

On CPython, it is possible to use
