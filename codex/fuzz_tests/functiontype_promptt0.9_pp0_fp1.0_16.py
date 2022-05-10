import types
# Test types.FunctionType check again!
def test_func() : pass
assert( isinstance(test_func, types.FunctionType))

import inspect
print(inspect.getsourcefile(test_func))

print(inspect.getmodule(test_func))

print(inspect.getmembers(test_func, inspect.ismethod))

# =============================================================================
# References:
# =============================================================================
