import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
keepalive= [a,b]
del a,b
def f(a):a.c.c=lst
keepalive.append(callback)
del keepalive
a=A()
a.x=a
