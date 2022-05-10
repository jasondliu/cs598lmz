import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
callback(a)
a=None
print keepali0e[0]() is None
keepali0e=None
import __builtin__,gc
print gc.get_referrers(__builtin__.__dict__)
print gc.collect()
import sys
import gc
print gc.get_threshold()
print gc.set_threshold(1,3,2)
print gc.get_threshold()
print gc.collect(0)
print gc.collect(1)
print gc.collect(2)
print gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)
def f():
    x=A()
    print x
f()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.set_debug(0)
print gc.get_debug()
print gc.set_debug(gc.DEBUG_STATS)
print gc.get_debug()
print gc.collect()
print gc.set_
