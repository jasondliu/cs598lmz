import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() works on weakref objects
# and that old weakrefs get cleared out correctly.

# A weak-available class()
class C:
    x = 6
    def __init__(self):
        self.x = 7
    def __del__(self):
        print "__del__ was called"

# Make an instance
o = C()

# Create some weak refs
wr1 = weakref.ref(o)
wr2 = weakref.ref(o)
wr3 = weakref.ref(o)

print "Before the cycle is broken"
print wr1(), wr2(), wr3()
print "There are %d weakrefs" % len(weakref.getweakrefs(o))
assert len(weakref.getweakrefs(o)) == 3

# Break the cycle and delete one of the
# weak-available instances, triggering a
# __del__
del o
print "After the cycle is broken"
print wr1(), wr2(), wr3()
print "There are %d weakrefs" % len(weakref.getweakrefs(
