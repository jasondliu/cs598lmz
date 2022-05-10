import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=weakref.ref(a,callback)
lst[0].c=lst
a.d=a
keepalive=[]
for i in xrange(100):
    a=A()
    a.c=a
    lst.append(weakref.ref(a,callback))
    lst[-1].c=lst
    keepalive.append(a)
del a,keepalive
import gc
gc.collect()
print(gc.garbage)

#print(lst['0'].deleting)
#print(lst['0'].dereferencable)
#print(lst['0'].dead)
#print(lst['0'].pendingcallbacks)
#print(lst['0'].alive)
