import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

f = Foo()
b = Bar()

print(gc.collect())

del f, b

print(gc.collect())

# Test gc.garbage

class Foo:
    pass

class Bar:
    pass

f = Foo()
b = Bar()

print(gc.garbage)

del f, b

print(gc.garbage)

# Test gc.get_referrers

class Foo:
    pass

class Bar:
    pass

f = Foo()
b = Bar()

print(gc.get_referrers(f))
print(gc.get_referrers(b))
print(gc.get_referrers(Foo))
print(gc.get_referrers(Bar))

del f, b

print(gc.get_referrers(Foo))
print(gc.get_referrers(Bar))

# Test gc.get_referents

class Foo:

