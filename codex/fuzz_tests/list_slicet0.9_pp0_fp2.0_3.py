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
import gc
assert not gc.collect()
class A(object):pass
import weakref
def callback(x):del lst[0]
a=A()
a.c=a
wr=weakref.ref(a,callback)
del a
lst=[str()]
while lst:lst[:]
import gc
assert not gc.collect()

def strong_ref(obj):
    """ return a strong reference to the object obj """
    return obj
def callback(x):
    del lst[0]
import weakref
import gc
obj = Dummy()
ref = weakref.ref(obj, callback)
lst = []
strong_ref(obj)
for i in range(1001):
    lst.append(str(i))
    strong_ref(obj)
strong_ref(obj)
a = strong_ref(obj)
assert a is obj
del lst[0]
gc.collect()
assert not gc.garbage
lst = []
strong_ref(obj)
try:
    import array
except
