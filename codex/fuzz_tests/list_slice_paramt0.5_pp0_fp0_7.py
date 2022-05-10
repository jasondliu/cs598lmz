import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print lst
print len(gc.get_referrers(lst))
print gc.get_referrers(lst)
del lst
gc.collect()
print gc.get_referrers(lst)
