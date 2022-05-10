import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wref=weakref.ref(a, callback)
del a
del keepalive[0]
gc.collect()
print wref()
print lst
