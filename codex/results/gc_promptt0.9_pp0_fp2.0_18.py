import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = []
b = [a]
a.append(b)
weakref.finalize(a, print, 'finalized a')
weakref.finalize(b, print, 'finalized b')
del a,b
gc.collect()               # Prints "finalized a".

# Test if gc is enabled
if gc.isenabled():
    # Disable automatic garbage collection.
    gc.disable()
    ...
    gc.enable()


import gc
gc.collect()
gc.set_debug(gc.DEBUG_STATS)

i=0
def kill():
    global i
    i+=1
    print(i)

a = []
b = [a]
a.append(b)
for _ in range(200):
    a.append(1)
    b.append(2)
    weakref.finalize(a, kill, 'finalized a')
    weakref.finalize(b, kill, 'finalized b')
    del a,b
    a = []
    b = [a]
   
