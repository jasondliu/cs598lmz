import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
#print lst
import gc
gc.collect()
print lst
keepali0e.append(weakref.ref(lst[0],callback))
del lst
gc.collect()
print keepali0e
#print lst
import weakref
class A(object):pass
a=A()
a.c=a
del a
#import gc
#gc.collect()

import gc

class A(object):pass
for i in xrange(5):
    a=A()
    a.c=a
    del a
gc.collect()
for i in xrange(5):
    a=A()
    a.c=a
    del a
    gc.collect()
for i in xrange(5):
    a=A()
    a.c=a
    del a

gc.collect()

for i in xrange(5):
    a=A()
    a.c=a
    del a
    gc.collect()


import gc
a=dict
