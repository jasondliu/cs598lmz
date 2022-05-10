import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
print len(gc.get_objects())
print len(gc.get_referrers(lst))
print len(gc.get_referrers(lst[0]))
print len(gc.get_referrers(lst[0],True))
print len(gc.get_referrers(lst[0],False))
print len(gc.get_referrers(lst[0],True,True))
print len(gc.get_referrers(lst[0],True,False))
print len(gc.get_referrers(lst[0],False,True))
print len(gc.get_referrers(lst[0],False,False))
print len(gc.get_referrers(lst[0],False,True,True))
print len(gc.get_referrers(lst[0],False,True,False))
print len(gc.get_referrers(lst[0],False,False,True))
print len(
