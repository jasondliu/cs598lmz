import gc, weakref

gc.set_debug(gc.DEBUG_SAVEALL)

class Foo:
    pass

class Bar:
    pass

# Create a few objects
f1 = Foo()
b1 = Bar()

# Create a few cycles
f1.x = f1
b1.x = b1

# Create a weak reference to a Foo
w = weakref.ref(f1)

# Clean up
del f1, b1

# Now we can call gc.garbage to see what the collector found.
# It should find a list containing the Foo and Bar
# objects and the reference cycle they are involved in.
print(gc.garbage)
