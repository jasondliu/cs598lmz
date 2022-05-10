import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst[0],callback))
del a
del lst
print('in callback',len(keepali0e))
import gc
gc.collect()
print('after gc',len(keepali0e))
print('will call callback',len(keepali0e))
keepali0e[0]=None
print('did call callback',len(keepali0e))
keepali0e[0]=None
print('did call callback',len(keepali0e))
keepali0e[0]=None
