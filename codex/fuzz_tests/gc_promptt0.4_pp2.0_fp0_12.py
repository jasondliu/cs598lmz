import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Test:
    def __init__(self):
        self.n = 1
    def __del__(self):
        print "Test.__del__"

t = Test()
t.n = 2
t.m = Test()
del t
gc.collect()

# Test gc.garbage
class Test:
    pass

t = Test()
t.n = 1
t.m = t
t.m.n = 2
t.m.m = t.m

gc.collect()
print gc.garbage

# Test gc.get_referrers
class Test:
    def __init__(self):
        self.n = 1
    def __del__(self):
        print "Test.__del__"

t = Test()
t.n = 2
t.m = Test()

print gc.get_referrers(t)
print gc.get_referrers(t.m)
print gc.get_referrers(t.m.n)

# Test gc.
