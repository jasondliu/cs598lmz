import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print len(lst)
print len(keepalive)
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
print keep
