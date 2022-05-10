gi = (i for i in ())
# Test gi.gi_code is None
ei = (i for i in ())
# Test ei.gi_code is None
assert ei.gi_code is None
import itertools

iter = itertools.chain((1, 2))
next(iter)
next(iter)
iter.gi_code = None

try:
    assert next(iter) == 1
except StopIteration:
    pass
else:
    # We expect StopIteration to be raised.
    raise AssertionError('StopIteration was not raised')
f = (i for i in ())
f.gi_frame
# Test that StopIteration passes through
next((i for i in ())), next((i for i in ()))
# Test that a generator returns itself as the iterator.
def gen():
    return (i for i in (1, 2))

outer_gen = gen()

inner_gen = next(outer_gen)

assert outer_gen is inner_gen
# Test gen.gi_code and gen.gi_frame
def gen():
#   import pdb; pdb.set_trace()
   
