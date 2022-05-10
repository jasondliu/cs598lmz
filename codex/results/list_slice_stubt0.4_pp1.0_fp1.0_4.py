import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
print(len(gc.get_referrers(lst)))
del lst
print(len(gc.get_referrers(lst)))
lst=[str()]
print(len(gc.get_referrers(lst)))
a=A()
a.c=a
lst.append(a)
print(len(gc.get_referrers(lst)))
del a
print(len(gc.get_referrers(lst)))
lst=None
print(len(gc.get_referrers(lst)))
lst=[str()]
print(len(gc.get_referrers(lst)))
a=A()
a.c=a
lst.append(a)
print(len(gc.get_referrers(lst)))
del a
print(len(gc.get_referrers(lst)))
lst=None
print(len(gc.get_referrers(lst)))
lst=[str
