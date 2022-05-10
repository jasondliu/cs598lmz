gi = (i for i in ())
# Test gi.gi_code
import sys
gi = (i for i in ())
code = gi.gi_code
# Make sure gi_code is a code object
import types
assert isinstance(code, types.CodeType)
# Test co_code
code = gi.gi_code
for c in code.co_code:
    assert isinstance(c, int)

# Test co_consts
consts = code.co_consts
# First const is None
assert consts[0] is None
# Second const is a code object
assert isinstance(consts[1], types.CodeType)
# Third const is a tuple containing a generator
assert isinstance(consts[2], tuple)
assert isinstance(consts[2][0], types.GeneratorType)

# Test co_names
names = code.co_names
# First name is 'StopIteration'
assert names[0] == 'StopIteration'
# Second name is 'GeneratorExit'
assert names[1] == 'GeneratorExit'

# Test co_varnames
varnames = code.co
