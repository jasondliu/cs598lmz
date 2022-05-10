import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c=lst
keepalive.append(a)
del a
gc.collect()
print len(lst)
print len(keepalive)
print len(gc.get_referrers(lst))
print len(gc.get_referrers(keepalive))
print len(gc.get_referrers(lst[0]))
print len(gc.get_referrers(keepalive[0]))
print len(gc.get_referrers(keepalive[1]))
print len(gc.get_referrers(keepalive[0].__dict__))
print len(gc.get_referrers(keepalive[1].__dict__))
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c=lst
keepalive.append(a)
del a
gc.collect()
print len(lst)
print len(keepal
