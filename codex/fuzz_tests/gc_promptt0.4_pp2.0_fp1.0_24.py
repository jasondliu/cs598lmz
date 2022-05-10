import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

a = A('a')
b = A('b')

a.b = b
b.a = a

print(gc.collect())
print(gc.collect())
print(gc.collect())

print(gc.garbage)

# Test gc.get_threshold()

print(gc.get_threshold())

# Test gc.get_count()

print(gc.get_count())

# Test gc.set_threshold()

gc.set_threshold(1, 2, 3)
print(gc.get_threshold())

# Test gc.get_debug()

print(gc.get_debug())

# Test gc.set_debug()

gc.set_debug(gc.DEBUG_STATS)
print(gc.get_debug())

gc.set_debug(0)
print(gc.get_debug())
