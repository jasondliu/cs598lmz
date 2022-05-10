import types
# Test types.FunctionType
def f(): pass
test(type(f) is types.FunctionType)
# Test types.LambdaType
test(type(lambda: None) is types.LambdaType)
# Test types.BuiltinFunctionType
test(type(len) is types.BuiltinFunctionType)
class C(object):
    pass
c = C()
c.f = f
# Test types.MethodType
test(type(c.f)  is types.MethodType)
test(type(C.f)  is types.UnboundMethodType)
def f(self): pass
test(type(f) is types.FunctionType)
# Test types.UnboundMethodType
test(type(f.__get__(3)) is types.MethodType)
test(type(f.__get__(3, int)) is types.MethodType)
print('ok')
