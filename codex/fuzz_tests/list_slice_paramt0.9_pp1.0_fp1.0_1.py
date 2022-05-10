import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a.c.c,callback))
keepali0e.append(weakref.ref(a.c.c.c,callback))
if sys.getrefcount(lst[0])>3:raise BaseException
del a
del keepali0e
gc.collect()
if not lst:raise BaseException
lst[0]=None
gc.collect()
if lst:raise BaseException
