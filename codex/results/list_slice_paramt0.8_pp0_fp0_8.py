import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
del a
del a.c
lst.append(a)
assert callback in weakref.getweakrefs(a)
lst.append(a.c)
assert callback in weakref.getweakrefs(a.c)
lst.append(a)
del keepali0e[:]
lst.append(a.c)
lst.append(a)
del a
import gc
gc.collect()
del a.c
del lst
for x in range(3):gc.collect()
lst=[x for x in gc.get_objects()if x]
assert len(lst)==0
del x, lst, gc, callback, keepali0e, weakref
del A
def f():
    x=[]
    class A(object):
        def __del__(self):x.append(1)
    a=A()
    a.c=a
    del a
def g():
    x=[]
    class A(object):
