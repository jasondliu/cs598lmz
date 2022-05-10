import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
keepali0e.append(lst[0])
del a,lst,callback
gc.collect()
print(len(gc.get_referrers(keepali0e[0])))
print(len(gc.get_referrers(keepali0e[1])))
print(len(gc.get_referrers(keepali0e[2])))
print(len(gc.get_referrers(keepali0e[3])))
print(len(gc.get_referrers(keepali0e[4])))
print(len(gc.get_referrers(keepali0e[0])))
print(len(gc.get_referrers(keepali0e[1])))
print(len(gc.get_referrers(keepali0e[2])))
print(len(gc.get_referrers(keepali0e[
