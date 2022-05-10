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
del lst
del keepali0e

import gc
gc.collect()
print(gc.garbage)

#2.2.2
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
 
del lst
del keepali0e
 
import gc
gc.collect()
print(gc.garbage)

#2.2.3
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
 
del keepali0e
 
import gc
gc.collect()
print(gc.garbage)

#2.2.4
import weakref
class A(object
