import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType
# Test types.GeneratorType
def f():
    yield 0

assert type(f()) is types.GeneratorType
# Test types.LambdaType
g = lambda: 1

assert type(g) is types.LambdaType
# Test types.ClassType
class C(object):
    pass

assert type(C) is types.ClassType
# Test types.UnboundMethodType
class D(object):
    def f(self):
        return 0

assert type(D.f) is types.UnboundMethodType
# Test types.MethodType
class E(object):
    def f(self):
        return 0

assert type(E().f) is types.MethodType
# Test types.BuiltinFunctionType
assert type(id) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
# Test types.DictProxyType
assert type(type.__dict__) is types.DictProxy
