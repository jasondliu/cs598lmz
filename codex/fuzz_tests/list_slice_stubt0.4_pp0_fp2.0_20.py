import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
keepalive.append(callback)
print(lst)
del a
del lst
del callback
print(keepalive)
gc.collect()
print(keepalive)
