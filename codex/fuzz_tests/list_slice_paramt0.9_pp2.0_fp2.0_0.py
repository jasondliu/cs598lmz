import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=(a,a,a)
del a
print('After del a,lst=',lst[0])
del lst[:]
lst=None
import gc
print('Begin gc.collect')
gc.collect()
print('End gc.collect')
