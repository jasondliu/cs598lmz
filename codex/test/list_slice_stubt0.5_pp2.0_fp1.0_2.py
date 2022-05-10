import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=A()
a.b.a=a
a.b.b=a.b
a.b.c=a
keepalive=[]
keepalive.append(a)
keepalive.append(a.b)
keepalive.append(a.b.a)
keepalive.append(a.b.b)
keepalive.append(a.b.c)
del a,A
keepalive.append(lst)
