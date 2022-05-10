import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
keepalive.append(a)
del a
print len(lst)
print lst
print lst[0]
print keepalive
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
print keepalive[0].c.c.c.c.c.c.c.c.c
