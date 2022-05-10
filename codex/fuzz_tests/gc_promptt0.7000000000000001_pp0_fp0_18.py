import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a (strong) cycle between a list and dict.
def create_cycle():
    l = [{}]
    l[0]['a'] = l
    return l

print('creating cycle...')
l = create_cycle()
print('done')
print('collecting...')
n = gc.collect()
print('done')
print('unreachable objects:', n)
print('strongly reachable objects:', len(gc.get_objects()))
print('weakly reachable objects:', len(gc.get_referrers(*gc.get_objects())))

# Test gc.collect() with a (strong) cycle between a list and a function
# (which is a function object, the function name is a reference to the
# function object).
def create_cycle2():
    # Function objects are directly reachable from the global dict
    # of the module.  But they are also reachable through their
    # __globals__ attribute, which refers to the module globals.
    l = [f]
    l[0] = l

print
