import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect:

class C:
    pass

x = C()
x.a = x
del x

gc.collect()

# Test gc.garbage:

class C:
    def __init__(self, n):
        self.n = n
    def __del__(self):
        print "collecting", self.n

gc.garbage[:]
for i in range(10):
    gc.garbage.append(C(i))

gc.collect()

class C:
    def __del__(self):
        print "collecting", self

gc.garbage[:]
gc.garbage.append(C())

gc.collect()

class C:
    def __init__(self, n):
        self.n = n
    def __del__(self):
        print "collecting", self.n

gc.garbage[:]
for i in range(10):
    gc.garbage.append(C(i))

gc.collect()

# Test gc.get_stats:


