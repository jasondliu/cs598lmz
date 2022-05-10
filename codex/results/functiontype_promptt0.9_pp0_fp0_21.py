import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
# Test types.LambdaType
assert type((lambda: None)) is types.LambdaType
# Test types.BuiltinFunctionType
f = min
assert type(f) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def f(): pass

assert type(C.f) is types.MethodType
c = C()
assert type(c.f) is types.MethodType

# Test types.UnboundMethodType
assert type(C.f) == type(C().f) == types.UnboundMethodType

# XXX: Does not work: Python functions are subtyped to built-in functions
# try: assert not isinstance(f, types.FunctionType)
# except: pass

try:
    print(types.FunctionType.__mro__)
except AttributeError as e:
    assert e.args[0] == "'tuple' object has no attribute '__mro__'"
    # CPython 3.x:
    # AttributeError:
