import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
wref=weakref.ref(a.c,callback)
del a
print 'del a'
import gc
gc.collect()
del keepali0e
print 'del keepalive'
for obj in gc.get_objects():
    print obj
    if isinstance(obj,A):
        print 'found A:%s' % str(obj)
print 'lst:',lst
