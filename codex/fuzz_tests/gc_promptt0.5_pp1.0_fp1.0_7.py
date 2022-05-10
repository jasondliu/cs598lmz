import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before and after weakref creation.

def callback(wr):
    print('callback(', wr, ')')

class MyClass:
    pass

mc = MyClass()

#
# Create cycles involving MyClass instances and a dict.
#
d = {}
for i in range(10):
    mc = MyClass()
    d[i] = mc
    d[mc] = i

#
# Create a cycle involving a weakref.
#
w = weakref.ref(mc, callback)
print('callback = ', callback)
print('w = ', w)

#
# Break the cycle.
#
del mc

#
# Force collection.
#
print('gc.collect() = ', gc.collect())
print('w = ', w)
print('callback = ', callback)

#
# Create a cycle involving a weakref and a list.
#
l = [MyClass(), MyClass(), MyClass()]
w = weakref.ref(l)
l.append(w)

#
# Break the cycle.
#
del l
