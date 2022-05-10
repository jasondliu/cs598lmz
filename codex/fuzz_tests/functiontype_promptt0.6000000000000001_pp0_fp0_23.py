import types
# Test types.FunctionType, types.MethodType, types.ClassType
def f(x):
    return x + 1

class C:
    def m(self, x):
        return x + 10

assert type(f) is types.FunctionType
assert type(C) is types.ClassType
assert type(C.m) is types.MethodType

# Test types.UnboundMethodType
assert type(C.m) is not types.UnboundMethodType
assert type(C.m) is types.MethodType
assert type(C.m.im_func) is types.FunctionType
assert type(C.m.im_self) is C
assert type(C.m.im_class) is types.ClassType

# Test types.LambdaType
assert type((lambda x: x)) is types.LambdaType

# Test types.GeneratorType
assert type((i for i in range(10))) is types.GeneratorType

# Test types.CodeType
def g(x):
    return x + 1

assert type(g.func_code) is types.CodeType

