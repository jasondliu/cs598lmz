import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
#a.b.c=a
#a.c.b=a
id(a)
id(a.b)
a.b.c.c.b.c
a.b is a.c
a.b.c is a
#a.b.b.c is a.b.c
#a.b.b.b.c is a.b.b.c
a.b.c.b.c is a.b.c
#a.b.b.b is a

#a.b.b.b.b is a.b.b
a.b.b is a.b.c.b
a.b.b is a.b
a.b.c.b is a.b.c
for n in range(1,10000000):
    a=A()
    a.c=a
    a.b=a
    a.b.c=a
    a.c.b=a
    a.b.c.c.b.c
    a.b is a.c
    a
