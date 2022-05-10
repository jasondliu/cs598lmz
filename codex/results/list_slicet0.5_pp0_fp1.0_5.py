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

# test_weakref_callbacks.py
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
def callback2(x):del lst[1]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback2))
del a
gc.collect()
while lst:keepali0e.append(lst[:])

# test_weakref_crash.py
import gc
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

# test_weakref_cycle_in_callback.py
import
