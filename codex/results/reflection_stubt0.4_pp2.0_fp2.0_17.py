fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This one is more interesting.  It's a generator expression, but it's
# never iterated.  The code object is not in the heap.
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This one is similar to the previous one, but the generator is
# iterated.  The code object is in the heap.
gi = (i for i in ())
gi.__next__()
fn.__code__ = gi.gi_code
fn()

# This one is similar to the previous one, but the generator is
# iterated twice.  The code object is in the heap.
gi = (i for i in ())
gi.__next__()
gi.__next__()
fn.__code__ = gi.gi_code
fn()

# This one is similar to the previous one, but the generator is
# iterated three times.  The code object is in the heap.
gi = (i for i in ())
gi.__next__()
gi.__next__
