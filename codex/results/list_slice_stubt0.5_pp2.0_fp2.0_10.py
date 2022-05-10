import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(A(),callback)
for i in range(10000):
    a=A()
    a.c=a
    keepalive.append(a)
    del a
    lst.append(str())
    del lst[0]
    print i
</code>


A:

You're creating a circular reference (a->b->a).  The weakref callback is only called when the last reference to an object is removed, and in this case, the last reference is the weakref itself.  The weakref callback is never called.

