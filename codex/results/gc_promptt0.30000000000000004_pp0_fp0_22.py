import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self, name):
        self.name = name

a = A('a')
b = A('b')
a.b = b
b.a = a

refs = [weakref.ref(x) for x in (a, b)]
del a, b
gc.collect()
for r in refs:
    print(r())

# Test gc.garbage

class A:
    def __init__(self, name):
        self.name = name

a = A('a')
b = A('b')
a.b = b
b.a = a

refs = [weakref.ref(x) for x in (a, b)]
del a, b
gc.collect()
for r in refs:
    print(r())

print(gc.garbage)

# Test gc.get_referrers

class A:
    def __init__(self, name):
        self.name = name

a = A('a')
b = A('
