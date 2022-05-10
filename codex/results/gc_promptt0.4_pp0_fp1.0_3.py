import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    def __del__(self):
        print "Deleting", self

c = C()
print "Collecting..."
gc.collect()
print "Collecting again..."
gc.collect()
print "Done."

print "Collecting..."
gc.collect()
print "Collecting again..."
gc.collect()
print "Done."

print "Collecting..."
gc.collect()
print "Collecting again..."
gc.collect()
print "Done."

# Test gc.garbage

class C:
    def __del__(self):
        print "Deleting", self

c = C()
gc.collect()
print gc.garbage

# Test gc.get_referrers()

class C:
    def __del__(self):
        print "Deleting", self

c = C()
print "Collecting..."
gc.collect()
print "Collecting again..."
gc.collect()
print "Done."

print "Collecting..."
gc.collect()
print "Collecting again..."
