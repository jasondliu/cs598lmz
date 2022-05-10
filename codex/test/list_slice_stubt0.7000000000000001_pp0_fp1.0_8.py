import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(a.c.c)
keepali0e.append(a.c.c.c)
keepali0e.append(a.c.c.c.c)
a.c.c.c.c.c=lst
del keepali0e
del a
del lst
