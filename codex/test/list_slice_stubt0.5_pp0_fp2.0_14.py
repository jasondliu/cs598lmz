import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
c=A()
c.c=a
a.b=b
b.b=c
c.b=a
a.a=a
b.a=b
c.a=c
keepali0e.append(a)
keepali0e.append(b)
keepali0e.append(c)
keepali0e.append(lst)
del a,b,c
