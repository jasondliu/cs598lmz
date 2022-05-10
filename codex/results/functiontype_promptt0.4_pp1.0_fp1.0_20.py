import types
# Test types.FunctionType

def f():
    pass

if type(f) != types.FunctionType:
    print("FAILED: type(f) != types.FunctionType")
    print("got:", type(f))
    print("expected:", types.FunctionType)
else:
    print("PASSED")

# Test types.BuiltinFunctionType

def g(x):
    return x

if type(g) != types.BuiltinFunctionType:
    print("FAILED: type(g) != types.BuiltinFunctionType")
    print("got:", type(g))
    print("expected:", types.BuiltinFunctionType)
else:
    print("PASSED")

# Test types.MethodType

class C:
    def f(self):
        pass

if type(C.f) != types.MethodType:
    print("FAILED: type(C.f) != types.MethodType")
    print("got:", type(C.f))
    print("expected:", types.MethodType)
else:
    print("PASSED
