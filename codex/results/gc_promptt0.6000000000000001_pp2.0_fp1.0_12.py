import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Test:
    def __init__(self, name):
        self.name = name
        print("Created", self.name)
t1 = Test("t1")
t2 = Test("t2")
t3 = Test("t3")
del t1, t2, t3
gc.collect()
# Test weakref
class Test:
    def __init__(self, name):
        self.name = name
        print("Created", self.name)
    def __del__(self):
        print("Deleted", self.name)
t = Test("t")
r = weakref.ref(t)
print("r:", r)
print("ref:", r())
print("t:", t)
del t
print("r:", r)
print("ref:", r())
# Test weakref
import gc
class Test:
    def __init__(self, name):
        self.name = name
        print("Created", self.name)
    def __del__(self):
        print("Deleted", self.name)
t
