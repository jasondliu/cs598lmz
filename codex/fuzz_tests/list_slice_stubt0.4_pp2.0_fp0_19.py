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
print(len(gc.get_referrers(lst)))
print(len(gc.get_referrers(lst[0])))
print(len(gc.get_referrers(keepalive[0])))
print(len(gc.get_referrers(keepalive[0].c)))
print(len(gc.get_referrers(callback)))
print(len(gc.get_referrers(keepalive)))
print(len(gc.get_referrers(lst)))
print(len(gc.get_referrers(lst[0])))
print(len(gc.get_referrers(keepalive[0])))
print(len(gc.get_referrers(keepalive[0].c)))
print(len(gc.get_referrers(callback)))
print(len(gc.get_referrers(keepalive)))
print(len(gc.get_referrers(lst)))
print(len(gc
