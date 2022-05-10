fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16984: Check that the code object of a generator is not
# accessible from the generator itself.
def g():
    yield
    yield
g.__code__ = None
g.gi_code = None
g.gi_frame = None
g.gi_running = None
g.gi_yieldfrom = None
g.gi_frame = None
g.gi_running = None
g.gi_yieldfrom = None
g.gi_frame = None
g.gi_running = None
g.gi_yieldfrom = None
g.gi_frame = None
g.gi_running = None
g.gi_yieldfrom = None
g.gi_frame = None
g.gi_running = None
g.gi_yieldfrom = None
g.gi_frame = None
g.gi_running = None
g.gi_yieldfrom = None
g.gi_frame = None
g.gi_running = None
g.gi_yieldfrom = None
g.gi_frame = None
g.gi_running =
