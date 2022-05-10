import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst[0]=a
keepalive.append(a)
del a
gc.collect()
del lst
gc.collect()
print keepalive
print callback
del keepalive
gc.collect()
print callback
del callback
gc.collect()
