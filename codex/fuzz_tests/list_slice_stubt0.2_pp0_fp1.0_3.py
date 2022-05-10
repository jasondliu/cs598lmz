import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
del a
del lst
gc.collect()
print gc.collect()
print len(gc.garbage)
print gc.garbage[0]
print gc.garbage[0].c
print gc.garbage[0].c.c
print gc.garbage[0].c.c.c
print gc.garbage[0].c.c.c.c
print gc.garbage[0].c.c.c.c.c
print gc.garbage[0].c.c.c.c.c.c
print gc.garbage[0].c.c.c.c.c.c.c
print gc.garbage[0].c.c.c.c.c.c.c.c
print gc.garbage[0].c.c.c.c.c.c.c.c.c
print gc.garbage[0].c.c.c.c.c.c.c.c.c
