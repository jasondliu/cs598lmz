fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Breakpoint 1

# For the next test, we'll set up a function that has a yield in it, but
# is not a generator function.  A normal function with a yield in it.
# We'll then set a breakpoint on that yield, and see if we stop there.

def fn():
    yield 0
    
# Breakpoint 2
fn()

# Now we'll set up a generator function, and a generator iterator, and
# see if we can set a breakpoint on the yield in the generator function,
# and see if we can stop there.

def fn():
    yield 0
    
gi = fn()

# Breakpoint 3
next(gi)

# Now we'll set up a generator function, and a generator iterator, and
# see if we can set a breakpoint on the yield in the generator function,
# and see if we can stop there.

def fn():
    yield 0
    
gi = fn()

# Breakpoint 4
gi.__next__()

# Now we'll set up a generator function, and a generator iterator,
