import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
keepalive.append(a)
keepalive.append(b)
c=A()
list.append(c)
c.c=lst
keepalive.append(c)
del a,b
gc.collect()
del c
