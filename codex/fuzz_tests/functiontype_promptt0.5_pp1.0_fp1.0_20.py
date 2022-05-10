import types
# Test types.FunctionType, which is the type of function objects

def f(): pass

print type(f) is types.FunctionType

print type(lambda: None) is types.FunctionType

print type(f) is types.FunctionType

print type(f.func_code) is types.CodeType

print type(f.func_globals) is types.DictType

print type(f.func_defaults) is types.TupleType

print type(f.func_closure) is types.TupleType

print type(f.func_doc) is types.StringType

print type(f.func_name) is types.StringType

# Check the type of a few builtin functions

print type(len) is types.BuiltinFunctionType

print type(list.append) is types.BuiltinMethodType

# Check the type of a few other builtin things

print type(None) is types.NoneType

print type(Ellipsis) is types.EllipsisType

print type(xrange(5)) is types.XRangeType


