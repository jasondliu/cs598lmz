import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
del a
del keepalive
</code>
This will trigger the callback, and delete the first element of lst. So it's possible to create a cyclic reference based on a weakref to an object which is destroyed when the reference is destroyed.

