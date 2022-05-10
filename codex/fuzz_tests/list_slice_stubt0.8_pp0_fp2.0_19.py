import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
del a
gc.collect()
len(gc.get_referrers(lst[0]))

def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
del a
gc.collect()
len(gc.get_referrers(lst[0]))

def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
weakref.ref(a,callback)
a.c=a
del a
gc.collect()
len(gc.get_referrers(lst[0]))

def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.v=weakref.ref(a,callback)
a.c=a
del a
gc.collect()
len(gc.get_referrers(lst[0]))

def callback(x):del lst[0]
keepalive=[]

