import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive
del lst
gc.collect()
</code>
I'm using Python 2.7.6.

