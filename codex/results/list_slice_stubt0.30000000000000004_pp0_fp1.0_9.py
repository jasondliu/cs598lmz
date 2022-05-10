import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print len(lst)
print lst
print keepalive
print len(keepalive)
print keepalive[0].c
print keepalive[0].c.c
print keepalive[0].c.c.c
print keepalive[0].c.c.c.c
print keepalive[0].c.c.c.c.c
print keepalive[0].c.c.c.c.c.c
print keepalive[0].c.c.c.c.c.c.c
print keepalive[0].c.c.c.c.c.c.c.c
print keepalive[0].c.c.c.c.c.c.c.c.c
print keepalive[0].c.c.c.c.c.c.c.c.c.c
print keepalive[0].c.c.c.c.c.c.c.c.c.
