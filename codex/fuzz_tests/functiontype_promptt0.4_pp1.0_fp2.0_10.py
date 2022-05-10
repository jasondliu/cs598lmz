import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
# Test types.MethodType
class C(object):
    def f(self): pass
c = C()
assert type(c.f) is types.MethodType
assert isinstance(c.f, types.MethodType)
# Test types.LambdaType
f = lambda : None
assert type(f) is types.LambdaType
assert isinstance(f, types.LambdaType)
# Test types.GeneratorType
def g(): yield None
assert type(g()) is types.GeneratorType
assert isinstance(g(), types.GeneratorType)
# Test types.CodeType
assert type(f.func_code) is types.CodeType
assert isinstance(f.func_code, types.CodeType)
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb
