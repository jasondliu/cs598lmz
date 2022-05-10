import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() at each opportunity.
gc.set_debug(gc.DEBUG_UNCOLLECTABLE |
             gc.DEBUG_INSTANCES |
             gc.DEBUG_OBJECTS |
             gc.DEBUG_STATS)

# The class to test.  It has a finalizer (read destructor) and,
# when deallocating, it changes an instance attribute of a global
# variable.
class Spam:
    def __del__(self):
        global x
        print("del", self, x)
        x = None

# Register a weakref callback on instance x.  When the callback is
# called, it will append the instance to the list L, and print it.
L = list()
def callback(x):
    print("callback of", x)
    L.append(x)

# We'll create a local variable, initialize it and then delete it,
# so that there is some garbage.  This will cause gc.collect() to
# run.  However, since we're running in verbose mode, it will print
# a line (just before calling collect),
