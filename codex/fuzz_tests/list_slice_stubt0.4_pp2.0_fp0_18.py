import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
print callback.__weakref__
del a
gc.collect()
print callback.__weakref__
print lst
print keepalive
print callback.__weakref__
del lst[0]
print callback.__weakref__
print lst
print keepalive
print callback.__weakref__
del keepalive[0]
print callback.__weakref__
print lst
print keepalive
print callback.__weakref__
