import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=A()
a.d.c=a
keepalive.append(a)
keepalive.append(a.d)
keepalive.append(a.d.c)
keepalive.append(a.d.c.d)
keepalive.append(lst)
del a
lst[0]=A()
lst[0].a=lst
lst[0].b=lst[0]
lst[0].c=lst[0]
lst[0].d=lst[0]
lst[0].e=lst[0]
lst[0].f=lst[0]
lst[0].g=lst[0]
lst[0].h=lst[0]
lst[0].i=lst[0]
lst[0].j=lst[0]
lst[0].k=lst[0]
lst[0].l=lst[0]
lst[0].m=lst[0]
lst[0
