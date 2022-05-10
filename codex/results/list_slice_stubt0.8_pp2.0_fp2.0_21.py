import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=weakref.proxy(a,callback)
del a
import gc
gc.collect()
print (lst)
#2.2有keepalive
#keepalive=[]
#lst=[str()]
#a=A()
#a.c=a
#lst[0]=weakref.proxy(a,callback)
#keepalive.append(a)
#del a
#import gc
#gc.collect()
#print(lst)

import weakref
class A(object):pass
def callback(x):print (1)
keepali0e=[]
lst=[str()]
a=A()
lst[0]=weakref.proxy(a,callback)
del a
import gc
gc.collect()
print (lst)
