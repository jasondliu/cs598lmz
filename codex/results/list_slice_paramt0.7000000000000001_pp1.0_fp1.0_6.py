import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(a,callback))
del a,callback
lst1=range(10)
lst2=range(10)
lst1.append(lst1)
lst2.append(lst2)
print len(gc.get_referrers(lst1))
print len(gc.get_referrers(lst2))
a=A()
a.c=A()
a.c.c=a
print len(gc.get_referrers(a))
print len(gc.get_referrers(a.c))
print len(gc.get_referrers(a.c.c))
a=A()
a.c=a
print len(gc.get_referrers(a))
print len(gc.get_referrers(a.c))
keepali0e=[]
lst=[str()]
lst.append(lst)
a=A()
a.c=a
keepali0e.append(weakref.ref(a
