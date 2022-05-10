import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))

import gc
gc.collect()
lst
dir(weakref)
dir(gc)
gc.set_threshold(1,1,1)
gc.set_debug(gc.DEBUG_LEAK)
gc.get_debug()
gc.get_threshold()
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
dir()
dir(__builtins__)
dir()
dir(__builtins__)
dir()
dir(__builtins__)
dir()
dir(__builtins__)
