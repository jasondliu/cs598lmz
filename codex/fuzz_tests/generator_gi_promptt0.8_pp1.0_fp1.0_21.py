gi = (i for i in ())
# Test gi.gi_code.co_freevars, gi.gi_code.co_cellvars
# and gi.gi_frame.f_locals
class Foo(object):
    pass
f = Foo()
f.a = 42
f.i = iter(f.a for _ in ())
test_freevars = f.i.gi_code.co_freevars
test_cellvars = f.i.gi_code.co_cellvars
test_code = f.i.gi_code
test_frame = f.i.gi_frame
test_funcname = f.i.gi_code.co_name
# generators should support __reduce__
def g():
    yield 1
    yield 2
    yield 3

class G(object):
    def __reduce__(self):
        return (g, ())

import pickle
for proto in range(pickle.HIGHEST_PROTOCOL + 1):
    try:
        pickle.loads(pickle.dumps(g(), proto))
        pickle.loads(pickle.dumps
