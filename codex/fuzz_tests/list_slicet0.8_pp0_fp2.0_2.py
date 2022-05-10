import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#пример 2.
import gc
class A(object):__slots__=('c',)
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,lambda x:del lst[0]))
del a
gc.collect()
while lst:keepalive.append(lst[:])
