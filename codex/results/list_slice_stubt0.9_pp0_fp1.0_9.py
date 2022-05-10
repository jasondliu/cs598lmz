import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=[a, a]
lst[0]=a
keepali0e.append(callback)
weakref.finalize(a, callback, lst)
gc.collect()
# assert len(lst)==0
keepalive(1)
del a
