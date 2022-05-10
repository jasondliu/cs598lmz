import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
lst

#gc.get_objects()
#gc.garbage

#gc.set_debug(gc.DEBUG_LEAK)
#gc.set_debug(gc.DEBUG_SAVEALL)
#gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
#gc.set_debug(gc.DEBUG_STATS)
#gc.set_debug(gc.DEBUG_COLLECTABLE)

#gc.get_debug()

#gc.enable()
#gc.disable()

#gc.isenabled()

#gc.collect()

#gc.set_threshold(700,10,5)

#gc.get_threshold()

#gc.get_objects()

#gc.get_count()

#gc.get_stats()

#gc.set_referrers(*objs)

#gc.get_referrers(*objs)

#gc.get_referents(*objs)

#gc.get_refer
