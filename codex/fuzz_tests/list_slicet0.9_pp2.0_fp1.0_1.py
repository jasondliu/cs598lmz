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
lst
import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE|gc.DEBUG_STATS)
def f():pass
def g():pass
h=[]
print ("before gc")
print h
f()
del f
gc.collect()
print ("after gc")
print h
g()
