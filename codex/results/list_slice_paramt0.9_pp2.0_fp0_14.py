import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
a.c=None
print(len(gc.get_referrers(keepali0e)))
a.r=weakref.ref(a,callback)
del a
