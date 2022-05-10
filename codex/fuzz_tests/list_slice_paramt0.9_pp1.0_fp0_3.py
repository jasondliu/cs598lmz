import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
</code>
But I can't figure out the cause.
PS: I'm using CPython 2.6.


A:

This is a known bug in Python 2.6 and 2.7: it is filed as bug #1336508 [Python 2.6] bug in reference.c:WR_REMOVE_HARD_WEAKREF() method.
This bug has been fixed in Python 3.2, but not backported to previous versions.

