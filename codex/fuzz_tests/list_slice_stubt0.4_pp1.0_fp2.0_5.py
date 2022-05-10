import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a.c,callback)
del a
del keepalive
gc.collect()
print lst

#['']

#这里有一个循环引用，没有被回收，所以lst中的引用也没有被回收

#改进：

import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a.c,callback)
del a
del keepalive
gc.collect()
print lst

#[]

#这里因为keepalive被删除了，所以a被
