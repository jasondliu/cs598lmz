import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive=[]
for i in range(10):
    b=A()
    b.a=a
    b.b=a
    b.c=a
    keepalive.append(b)
    keepalive.append(a)
    a=b
del a
del b
keepalive=[]
for i in range(10):
    b=A()
