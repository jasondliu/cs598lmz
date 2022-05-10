import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect at a finer granularity.
gc.enable()

#collect literals 
wr = weakref.ref(1)
print gc.collect()

i = 1
#collect literals again
wr = weakref.ref(1)
print gc.collect()
del i

#collect literals
wr = weakref.ref(1)
print gc.collect()
del wr

#collect true objects
wr = weakref.ref(object)
print gc.collect()
del wr

#collect reclaimed objects
#after flagging, the item must stay alive for another collection
#before being reclaimed
i = []; wr = weakref.ref(i)
print gc.collect(); del wr
print gc.collect(); del i

print gc.collect(); del wr

#collect reclaimed objects
#flagging causes more garbage to be collected, but garbage
#at the end remains
i = []; wr = weakref.ref(i)
print gc.collect(); del i, wr

print gc.collect(); del i, wr
