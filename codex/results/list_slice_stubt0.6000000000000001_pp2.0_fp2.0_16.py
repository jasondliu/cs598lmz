import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
del keepalive
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.collect()
print len(gc.garbage)
