import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]='a'
lst.append(weakref.ref(lst,callback))
lst.append(weakref.ref(lst,callback))
del lst
import gc
gc.collect()
print('ok')
