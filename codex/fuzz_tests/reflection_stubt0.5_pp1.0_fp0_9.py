fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Verify that the generator's __del__ method is called.

def g():
    yield 1

g.__del__ = lambda self: print("DEL")
del g()

# Verify that the generator's __del__ method is called when the generator
# is not yet exhausted.

def g():
    yield 1
    yield 2

g.__del__ = lambda self: print("DEL")
g = g()
next(g)
del g

# Verify that the generator's __del__ method is called when the generator
# is not yet exhausted and the generator is referenced by other objects.

def g():
    yield 1
    yield 2

g.__del__ = lambda self: print("DEL")
g1 = g()
g2 = g1
next(g1)
del g1
del g2

# Verify that the generator's __del__ method is called when the generator
# is not yet exhausted and the generator is referenced by other objects,
# and the generator's __del__ method references the generator.

def g():
   
