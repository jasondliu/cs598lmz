import types
# Test types.FunctionType
#
# Test that types.FunctionType returns the correct type for functions.
#
# Python version used: 2.7
#

import types

def func(x):
    return x

assert type(func) == types.FunctionType
assert type(lambda x: x) == types.FunctionType
