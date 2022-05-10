import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
print len(lst)
lst[0]=weakref.ref(lst,callback)
print len(lst)
del lst
print 'after del lst'
import gc
gc.collect()
print 'after collect'
print len(keepalive)
del keepalive[0]
print 'after del keepalive[0]'
gc.collect()
print 'after collect'
print len(keepalive)
del keepalive[0]
print 'after del keepalive[0]'
gc.collect()
print 'after collect'
print len(keepalive)
del keepalive[0]
print 'after del keepalive[0]'
gc.collect()
print 'after collect'
print len(keepalive)
del keepalive[0]
print 'after del keepalive[0]'
gc.collect()
print 'after collect'
print len(keepalive)
del keepalive[0]
print 'after del keepalive[0]'
gc.collect()
print
