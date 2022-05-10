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
print lst
print keepalive
print len(gc.get_referrers(lst))
print len(gc.get_referrers(keepalive))
print len(gc.get_referrers(lst[0]))
print len(gc.get_referrers(keepalive[0]))
print len(gc.get_referrers(lst[0].c))
print len(gc.get_referrers(keepalive[0].c))
print len(gc.get_referrers(lst[0].c.c))
print len(gc.get_referrers(keepalive[0].c.c))
print len(gc.get_referrers(lst[0].c.c.c))
print len(gc.get_referrers(keepalive[0].c.c.c))
print len(gc.get_referrers(lst[0].c.c.c.c
