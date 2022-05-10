import types
# Test types.FunctionType and types.LambdaType.

assert isinstance(lambda: 3, types.FunctionType)
assert isinstance(lambda: 3, types.LambdaType)

# Test types.GeneratorType

def gen():
    yield 1

assert isinstance(gen(), types.GeneratorType)

# Test types.BuiltinFunctionType

assert isinstance(abs, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)

# Test types.BuiltinMethodType

assert isinstance(list.append, types.BuiltinMethodType)
assert isinstance(dict.setdefault, types.BuiltinMethodType)

assert types.BuiltinFunctionType == type(list.append)
assert types.BuiltinMethodType == type(dict.setdefault)

# Test types.ModuleType

import sys
assert isinstance(sys, types.ModuleType)
assert isinstance(types, types.ModuleType)
assert isinstance(__name__, types.ModuleType)

# Test types.TracebackType

try:
    raise RuntimeError
