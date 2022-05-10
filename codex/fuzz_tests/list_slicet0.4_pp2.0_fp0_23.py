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
I'm using Python 2.7.3 on Windows 7.


A:

You're running into a known issue with the CPython implementation of weakrefs. The issue is that the <code>weakref</code> module is implemented in C, and the C implementation of weakrefs doesn't know about cycles.
The <code>weakref</code> module is implemented in C because the standard Python implementation of weakrefs is very slow. The C implementation is much faster, but it doesn't handle cycles.
The solution is to not use the C implementation of weakrefs. You can do that by importing <code>weakref</code> from the <code>_weakrefset</code> module instead of from the <code>weakref</code> module.
<code>from _weakrefset import weakref
</code>

