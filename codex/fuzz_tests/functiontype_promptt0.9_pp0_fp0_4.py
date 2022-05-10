import types
# Test types.FunctionType only, because the other types are native
assert types.FunctionType._itemsize_ == 0
assert type(types.FunctionType) == types.TypeType

# new-style class
assert type(__builtins__.__import__) == type
assert type(__builtins__.__import__) == types.BuiltinFunctionType
assert issubclass(types.BuiltinFunctionType, object)
assert types.BuiltinFunctionType._itemsize_ == 0
assert __builtins__.__import__._itemsize_ == 0

# old-style class
assert type(list.append) == types.MethodType
assert type(list.append) != type
assert type(list.append) == types.BuiltinMethodType
assert issubclass(types.BuiltinMethodType, object)
assert not isinstance(list.append, object)
assert types.BuiltinMethodType._itemsize_ == 0

class A(object):
    class B(object):
        s = "foo"

assert A.B.__dict__ == {"s": "foo"}
assert A.__dict__ == {}

