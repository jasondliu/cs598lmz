import types
# Test types.FunctionType

def f(): pass

f_type = type(f)

assert isinstance(f, f_type)
assert f_type is types.FunctionType

try:
    f_type()
except TypeError:
    print("TypeError")

# Test types.BuiltinFunctionType

try:
    types.BuiltinFunctionType()
except TypeError:
    print("TypeError")

import sys

assert type(len) is types.BuiltinFunctionType
assert type(sys.exit) is types.BuiltinFunctionType
assert type(chr) is types.BuiltinFunctionType
assert type(ord) is types.BuiltinFunctionType
assert type(repr) is types.BuiltinFunctionType
assert type(range) is types.BuiltinFunctionType
assert type(print) is types.BuiltinFunctionType
assert type(filter) is types.BuiltinFunctionType
assert type(map) is types.BuiltinFunctionType
assert type(zip) is types.BuiltinFunctionType
assert type(sorted) is types.BuiltinFunctionType
assert type(any) is
