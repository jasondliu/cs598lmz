import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
del a
gc.collect()
print lst
print len(gc.get_referrers(lst))
print len(gc.get_referrers(lst[0]))
print len(gc.get_referrers(lst[1]))
print len(gc.get_referrers(lst[1].c))
print len(gc.get_referrers(lst[1].c.c))
print len(gc.get_referrers(lst[1].c.c.c))
print len(gc.get_referrers(lst[1].c.c.c.c))
print len(gc.get_referrers(lst[1].c.c.c.c.c))
print len(gc.get_referrers(lst[1].c.c.c.c.c.c))
print len(gc.get_referrers(lst[1].c.c.c.c.c.c.c))
