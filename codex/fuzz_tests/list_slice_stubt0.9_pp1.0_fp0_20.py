import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
callback(keepali0e)
del a.c
gc.collect()


from itertools import chain
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
callback(keepali0e)
del a.c
gc.collect()


set = set()
def f():
    pass
f = lambda: f; f().next = f
set.add(f)
del f
gc.collect()


# test out the weakref support for objects with __len__() methods defined
import weakref,gc

class MyObject(object):
    def __len__(self):
        return 42

o = MyObject()
r = weakref.ref(o)

o_id = id(o)

del o
gc.collect()
gc.collect()

o = r()
assert o_id == id(o)


import weakref,gc
def callback(x):
    print 'callback called!'
    del lst[0]
    
ref
