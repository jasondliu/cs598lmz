import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=lst
lst[0]=weakref.ref(lst,callback)
del lst
import gc
gc.collect()
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
print keepalive[0].c.c.c.c.c.
