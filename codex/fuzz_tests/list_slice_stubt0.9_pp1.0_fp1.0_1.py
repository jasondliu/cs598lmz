import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wrattrs={wr for wr in dir(weakref) if not wr.startswith("__")}
del keepalive, wrattrs
wrf=weakref.ref(a,callback)
wrm=weakref.WeakMethod(wrf)
del wrattrs
del wrf, callback
lst=None
del lst
wrm=None
del wrm
del a
gc.collect(2)
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.b=a
a.c=a
a.d=a
keepalive.append(a)
wrattrs=[wr for wr in dir(weakref) if not wr.startswith("__")]
wrf=weakref.ref(a.b,callback)
wrm=weakref.WeakMethod(wrf)
del a.d
del wrattrs
del wrf, callback
a.c=None
a.d=None
a
