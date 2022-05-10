import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print lst
a=None
print lst
print keepalive
print keepalive[0].c
print keepalive[0].c is keepalive[0]
print keepalive[0].c.c
print keepalive[0].c.c is keepalive[0]
print keepalive[0].c.c.c
print keepalive[0].c.c.c is keepalive[0]
print keepalive[0].c.c.c.c
print keepalive[0].c.c.c.c is keepalive[0]
print keepalive[0].c.c.c.c.c
print keepalive[0].c.c.c.c.c is keepalive[0]
print keepalive[0].c.c.c.c.c.c
print keepalive[0].c.c.c.c.c.c is keepalive[0]
print keepal
