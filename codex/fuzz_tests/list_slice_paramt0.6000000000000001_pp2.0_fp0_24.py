import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
lst

# gc.garbage

a = A()
a.c = a
keepalive = [a]
del a
import gc
gc.collect()
gc.garbage

# gc.garbage

lst = [str()]
a = A()
a.c = a
keepalive = [a]
del a
import gc
gc.collect()
gc.garbage

# gc.garbage

lst = [str()]
a = A()
a.c = a
keepalive = [a]
del a
import gc
gc.collect()
gc.garbage

# gc.garbage

lst = [str()]
a = A()
a.c = a
keepalive = [a]
del a
import gc
gc.collect()
gc.garbage

# gc.garbage

lst = [str()]
