import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Class:
    def __init__(self):
        self.l = [1, 2, 3]
    def __del__(self):
        print("deleted")

c = Class()
r = weakref.ref(c)
print(r())
del c
print(r())
gc.collect()
print(r())

# Test cyclic gc

class Class:
    def __init__(self):
        self.l = [1, 2, 3]
    def __del__(self):
        print("deleted")

c = Class()
r = weakref.ref(c)
c.r = r
print(r())
del c
print(r())
gc.collect()
print(r())

# Test finalize

class Class:
    def __init__(self):
        self.l = [1, 2, 3]
    def __del__(self):
        print("deleted")

def callback(r):
    print("callback")

c = Class()
r = weakref.finalize
