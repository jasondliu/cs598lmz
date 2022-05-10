gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
try:
    next(gi)
except:
    pass

gi.gi_code is None
gi.gi_frame is None

# Test that closing an iterator doesn't crash
iter(lambda: 1).__next__().__del__()

# Test that generator-iterator's refcount is properly increased
# when the generator is called from multiple frames
def f():
    g = ((1, i) for i in range(2))

    next(g)
    next(g)

f()
f()

# Test that a generator-iterator's deallocator doesn't crash when
# its frame is freed
def f(n):
    return ((1, i) for i in range(n))

next(f(1))
next(f(1))

# Test that a generator-iterator's deallocator can handle being called
# when the frame object is on the stack, even if it's corrupted
import sys
from test import support

def f():
    g = iter(lambda: 1, 1)

    next(g)

def my
