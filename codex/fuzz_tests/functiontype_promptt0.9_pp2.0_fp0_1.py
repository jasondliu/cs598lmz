import types
# Test types.FunctionType
# Last update: 11/23/2010
#Bug#1147492
import __main_class__
a = function1
assert isinstance(a, types.FunctionType)

b = types.FunctionType
assert not isinstance(a, b)
