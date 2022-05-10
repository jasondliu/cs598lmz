import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(lst[0],callback))
lst.append(weakref.ref(a.c,callback))
del lst
import gc;gc.collect()
print keepalive
print len(keepalive)
del keepalive[0]
print len(keepalive)
