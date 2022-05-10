import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0] = weakref.ref(a)
lst[0].addCallback(callback)
b=A()
b.c=b
keepalive.append(b)
del b
del keepalive
del a
print lst[0]()
