import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
a.e=str()
a.f=str()
obj=lst[0]
obj_id=id(obj)
print obj,obj_id
keepali0e.append(obj)
del obj
wref=weakref.ref(a,callback)
lst.append(wref)
print keepali0e
print lst
len(gc.get_referrers(keepali0e[0]))
del lst
print keepali0e
print len(gc.get_referrers(keepali0e[0]))
del lst
print keepali0e
print len(gc.get_referrers(keepali0e[0]))
