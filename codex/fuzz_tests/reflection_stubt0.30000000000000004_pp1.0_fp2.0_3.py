fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: Make sure that the code object of a generator is
# properly cleared when the generator is finalized.
gc.collect()
import weakref
wr = weakref.ref(gi)
del gi
gc.collect()
assert wr() is None

# Issue #24071: Make sure that the code object of a generator is
# properly cleared when the generator is finalized.
gc.collect()
import weakref
wr = weakref.ref(gi)
del gi
gc.collect()
assert wr() is None

# Issue #24071: Make sure that the code object of a generator is
# properly cleared when the generator is finalized.
gc.collect()
import weakref
wr = weakref.ref(gi)
del gi
gc.collect()
assert wr() is None

# Issue #24071: Make sure that the code object of a generator is
# properly cleared when the generator is finalized.
gc.collect()
import weakref
wr = weakref.ref(gi)
del gi
gc.collect()
assert wr()
