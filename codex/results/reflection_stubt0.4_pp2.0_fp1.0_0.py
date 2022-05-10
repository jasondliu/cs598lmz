fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a tricky case.  The code object is not a code object, but a generator.
# The generator is not empty, so we can't just skip it.  We also don't want to
# call it, because then we'd end up in an infinite loop.  So we just skip the
# generator.

# We could try to be more clever and check to see if the generator is empty, and
# if so, just skip it.  But I think this is good enough.

fn = lambda: None
gi = (i for i in ())
gi.__code__ = fn.__code__
fn()

# This is a tricky case.  The code object is not a code object, but a generator.
# The generator is not empty, so we can't just skip it.  We also don't want to
# call it, because then we'd end up in an infinite loop.  So we just skip the
# generator.

# We could try to be more clever and check to see if the generator is empty, and
# if so, just skip it.  But I think this is
