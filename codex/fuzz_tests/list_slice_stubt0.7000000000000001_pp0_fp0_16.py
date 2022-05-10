import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst[0]=weakref.ref(a.b,callback)
del a
del a
import gc
gc.collect()
print('done')
