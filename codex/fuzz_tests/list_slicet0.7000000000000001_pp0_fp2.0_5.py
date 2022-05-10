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
but it doesn't work.


A:

This is a well-known bug in <code>CPython</code>'s <code>weakref</code> module.
More info here:
http://bugs.python.org/issue5339

