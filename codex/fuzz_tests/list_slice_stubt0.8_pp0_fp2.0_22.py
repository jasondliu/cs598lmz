import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
lst[0]=a
del lst
gc.collect()
assert len(gc.garbage)==2
gc.garbage[0].c=gc.garbage[1]
gc.garbage=None
weakref.ref(gc.garbage,callback)
del a,keepalive
gc.collect()
