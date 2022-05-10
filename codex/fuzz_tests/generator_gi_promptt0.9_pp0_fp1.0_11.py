gi = (i for i in ())
# Test gi.gi_code is code or not
code_types = type(gi.gi_code), types.MethodType
assert isinstance(gi.gi_code, code_types)
gi = (i for i in ())
# Test func_code is code or not
code_types = type(gi.__code__), types.MethodType
assert isinstance(gi.__code__, code_types)

digits = range(10)
digits_iter = iter(digits)
# Test iterobject.gi_code is code or not
code_types = type(digits_iter.gi_code), types.MethodType
assert isinstance(digits_iter.gi_code, code_types)
digits_iter = iter(digits)
# Test iterobject.__code__ is code or not
code_types = type(digits_iter.__code__), types.MethodType
assert isinstance(digits_iter.__code__, code_types)

# Test iterator information about generators
def foo():
  return (x*x for x in range(5))

g1 = foo()
g
