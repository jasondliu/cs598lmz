import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
lst[0]=lst
lst[0].append(a)
lst[0].append(a)
del lst
del keepalive
import gc
gc.collect()
print gc.collect()
print gc.garbage
print len(gc.garbage)
print gc.get_referrers(a)
print gc.get_referrers(a, str)
print gc.get_referrers(a, str, 1)
print gc.get_referrers(a, str, 2)
print gc.get_referrers(a, str, 3)
print gc.get_referrers(a, str, 4)
print gc.get_referrers(a, str, 5)
print gc.get_referrers(a, str, 6)
print gc.get_referrers(a, str, 7)
print gc.get_referrers(a, str, 8)
print g
