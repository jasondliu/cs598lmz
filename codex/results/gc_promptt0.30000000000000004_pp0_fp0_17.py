import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "deleting", self.x

f = Foo(1)
f.y = Foo(2)
f.z = Foo(3)

print gc.collect()
print gc.collect()
del f
print gc.collect()
print gc.collect()

# Test gc.garbage

class Foo(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "deleting", self.x

f = Foo(1)
f.y = Foo(2)
f.z = Foo(3)

print gc.collect()
print gc.collect()
del f
print gc.collect()
print gc.collect()

# Test gc.get_referrers

class Foo(object):
    def __init__(self, x):
        self.x = x
   
