import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f, types.FunctionType), \
       "f is not a function"

# Test types.MethodType

class C:
    def f(self):
        pass

assert isinstance(C.f, types.MethodType), \
       "C.f is not a method"

assert isinstance(C().f, types.MethodType), \
       "C().f is not a method"

# Test types.UnboundMethodType

assert isinstance(C.f, types.UnboundMethodType), \
       "C.f is not an unbound method"

# Test types.BuiltinFunctionType

assert isinstance(type, types.BuiltinFunctionType), \
       "type is not a builtin function"

assert isinstance(C.f.im_func, types.BuiltinFunctionType), \
       "C.f.im_func is not a builtin function"

# Test types.BuiltinMethodType

assert isinstance(type, types.BuiltinMethodType), \
       "type
