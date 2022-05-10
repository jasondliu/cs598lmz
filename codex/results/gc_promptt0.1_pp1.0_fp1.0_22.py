import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    print('in bar')
    f = Foo()
    wr = weakref.ref(f, bar)
    print('leaving bar')

bar()
gc.collect()
print('end of test')

# Test gc.garbage

class Foo:
    pass

def bar():
    print('in bar')
    f = Foo()
    wr = weakref.ref(f, bar)
    print('leaving bar')

bar()
print(gc.garbage)
print('end of test')

# Test gc.get_debug()

print(gc.get_debug())

# Test gc.get_objects()

print(len(gc.get_objects()))

# Test gc.get_referrers()

print(len(gc.get_referrers(gc)))

# Test gc.get_threshold()

print(gc.get_threshold())

# Test gc.is_tracked()

print(gc.is
