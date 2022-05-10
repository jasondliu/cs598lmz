gi = (i for i in ())
# Test gi.gi_code.co_lnotab
gi.gi_code.co_lnotab

# Test gi.gi_code.co_code
gi.gi_code.co_code

# Test gi.gi_frame.f_trace_opcodes if available
if hasattr(gi.gi_frame, 'f_trace_opcodes'):
    gi.gi_frame.f_trace_opcodes

# Check creation reference by creating one and calling
# gc.collect().  This is a bit hacky, but we can't
# reliably create a reference and then delete it, since
# we don't know how the C code works.
#
# At the time of writing, no test fails if the following
# is commented out, but the test suite will leak memory
# in the case of a failure.  This test should be cleaned
# up to either fail more visibly or fail without leaking
# memory.

#import gc
#gc.collect()
#gc.collect()

def gen():
    yield
    yield
    yield
    yield

g = gen()

del g
