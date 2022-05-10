import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
keepalive0=[a]
del a
del keepalive
gc.collect()
print len(gc.get_objects())
print gc.collect()
print len(gc.get_objects())
