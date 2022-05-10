import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=a
keepalive.append(weakref.ref(lst[0],callback))
del lst
del keepalive
del callback
</code>

