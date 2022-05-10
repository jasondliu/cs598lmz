fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Ensure that the code object is not freed while the generator is still
# alive.
import gc
gc.collect()
fn()

# Ensure that the generator is freed when the code object is freed.
del fn
gc.collect()
fn()
