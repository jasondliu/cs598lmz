import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
del keepalive
gc.collect()
print 'after collect:',gc.collect()
print 'unreachable:',gc.garbage
print 'unreachable:',gc.garbage[0]
print 'unreachable:',gc.garbage[0].c
print 'lst:',lst
print 'lst[0]:',lst[0]
print 'lst[0]:',lst[0].c
print 'lst[0]:',lst[0].c.c
print 'lst[0]:',lst[0].c.c.c
print 'lst[0]:',lst[0].c.c.c.c
print 'lst[0]:',lst[0].c.c.c.c.c
print 'lst[0]:',lst[0].c.c.c.c.c.c
print 'lst[0]:',lst[0].c.c.c.c.c.c.c
print 'lst[0]:',
