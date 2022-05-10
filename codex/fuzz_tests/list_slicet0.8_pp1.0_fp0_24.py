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
print(len(keepali0e))
import gc
gc.collect()
print(len(keepali0e))
import gc
import weakref
a=str()
ref=weakref.ref(a,lambda:print('callback called'))
print(ref())
del a
gc.collect()
class A(object):pass
a=A()
b=A()
a.b=b
b.b=a
del a
print(gc.get_referrers(b))
class A(object):pass
a=A()
del a
print(gc.get_objects())
import weakref
a=A()
b=A()
a.b=b
b.a=a
del a
del b
c=A()
print(gc.get_referrers(c))
print(gc.get_referrers(c,1))
print(gc.get_referrers(c,2))
import gc
print(gc.garbage)
class A(object):pass
a=A()
b=A()
a.b
