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
import gc;gc.collect()
print len(keepali0e)
print keepali0e
#del lst
#del lst[0]

#second way
import gc
import weakref
class A:pass
a=A()
a.x=a
weakref.ref(a,lambda r:print(r))
del a
while 1:
    gc.collect()
