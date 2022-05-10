import types
# Test types.FunctionType, if it exists.
if hasattr(types, 'FunctionType'):
    def func():
        pass
    assert type(func) is types.FunctionType
# Test types.BuiltinFunctionType, if it exists.
if hasattr(types, 'BuiltinFunctionType'):
    assert type(len) is types.BuiltinFunctionType
# Test types.MethodType, if it exists.
if hasattr(types, 'MethodType'):
    l = []
    assert type(l.append) is types.MethodType
# Test types.BuiltinMethodType, if it exists.
if hasattr(types, 'BuiltinMethodType'):
    assert type([].append) is types.BuiltinMethodType
# Test types.UnboundMethodType, if it exists.
if hasattr(types, 'UnboundMethodType'):
    assert type(list.append) is types.UnboundMethodType

# Test that the return values of type() and isinstance() are properly cached
# and do not grow without bound (refs #11086 and #16993)

class A(object):
   
