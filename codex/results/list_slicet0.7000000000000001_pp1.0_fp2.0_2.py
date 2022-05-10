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
On my computer, this code runs for a minute or two, then starts throwing <code>RecursionError: maximum recursion depth exceeded</code>, which means the callback has executed, or at least attempted to.
This means that while <code>weakref</code>s are not garbage collected when they refer to garbage-collectable objects, they can be collected when they refer to non-collectable objects.

So, what is going on here?
<code>weakref.ref</code>s are themselves garbage-collectable, and are in fact collected when they refer to garbage-collectable objects.
However, <code>weakref.ref</code>s are not collected when they refer to non-garbage-collectable objects.

