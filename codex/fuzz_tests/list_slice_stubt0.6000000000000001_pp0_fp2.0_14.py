import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
b=A()
b.c=a
keepalive.append(b)
lst.append(weakref.ref(b,callback))
del lst
del keepalive
del b
del a
del callback
</code>

