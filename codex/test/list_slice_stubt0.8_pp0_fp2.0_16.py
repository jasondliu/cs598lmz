import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
p=weakref.proxy(a,callback)
keepali0e.append(p)
b=p.c
c=b.c
d=c.c
