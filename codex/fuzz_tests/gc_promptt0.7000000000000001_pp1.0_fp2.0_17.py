import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
for x in range(3):
    print('Collecting')
    n = gc.collect()
    print('Unreachable objects:', n)
    print('Remaining Garbage:', end=' ')
    pprint(gc.garbage)
    print('gc.garbage[0] = 1')
    gc.garbage[0] = 1
    print('Remaining Garbage:', end=' ')
    pprint(gc.garbage)

# Test gc.callbacks
def callback(ignored):
    print('Called back', gc.collect())
    print('Unreachable objects:', gc.collect())
    print('Remaining Garbage:', end=' ')
    pprint(gc.garbage)

print('Registering callbacks')
gc.callbacks.append(callback)
gc.callbacks.append(callback)
print('done')

print('Enabling collection')
gc.enable()
print('done')

print('Collecting')
gc.collect()
print('done')

print('Disabling collection
