import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
a.e=a
keepalive=[]
lst.append(a)
keepalive.append(a)
keepalive.append(lst)
keepalive.append(callback)
keepalive.append(callback)
keepalive.append(keepalive)
weakref.ref(a,callback)
keepalive.append(a)
del keepalive
del a
del lst
del keepalive
gc.collect()
print(gc.collect())
print(gc.garbage)
