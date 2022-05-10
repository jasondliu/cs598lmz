fn = lambda: None
# Test fn.__code__.co_varnames
self.fn.__code__.co_varnames = tuple('abc')
# Validate the result
self.assertEqual(self.fn.__code__.co_varnames, tuple('abc'))

# Test Set/Get co_argcount
self.fn = lambda: None
# Test co_argcount
self.fn.__code__.co_argcount = 5
# Validate the result
self.assertEqual(self.fn.__code__.co_argcount, 5)

# Test Set/Get co_cellvars
self.fn = lambda: None
# Test co_cellvars
self.fn.__code__.co_cellvars = tuple('abc')
# Validate the result
self.assertEqual(self.fn.__code__.co_cellvars, tuple('abc'))

# Test Set/Get co_code
from dis import get_instructions
def fn():
    pass
code = get_instructions(fn)
code[0] = (code[0][0],
