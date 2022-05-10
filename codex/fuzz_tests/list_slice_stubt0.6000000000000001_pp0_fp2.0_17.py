import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
w=weakref.ref(a,callback)
del a
while lst:pass
</code>
This is the only way I can see to get the cyclic reference to be removed.
I'm not sure if this is a bug in Python or the CPython implementation.

