import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
gc.collect()
print lst
print keepalive
print len(gc.get_referrers(keepalive[0]))
print len(gc.get_referrers(keepalive[0],lst))
print gc.get_referrers(keepalive[0])
print gc.get_referrers(keepalive[0],lst)
print gc.get_referrers(lst[0])
print gc.get_referrers(lst[0],lst)
print gc.get_referrers(lst[1])
print gc.get_referrers(lst[1],lst)
