import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self):
        pass

assert type(C.m) == types.MethodType
assert type(C().m) == types.MethodType

# Test types.BuiltinMethodType
assert type(C.__init__) == types.BuiltinMethodType
assert type(C().__init__) == types.BuiltinMethodType

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType
assert type(x for x in range(10)) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType
assert type(lambda: None).__code__ == types.CodeType

# Test types.TracebackType
try:
    1 / 0
except:
    tb = sys.exc_info()[2]
    assert type
