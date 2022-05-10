import types
# Test types.FunctionType
def f1(x):
    return x + 1
# Test types.LambdaType
f2 = lambda x: x + 1
# Test types.GeneratorType
def f3():
    yield 1
gen = f3()
# Test types.BuiltinFunctionType
print types.BuiltinFunctionType
# Test types.BuiltinMethodType
print types.BuiltinMethodType
class A(object):
    def func(self):
        pass
a = A()
print types.BuiltinMethodType(a.func, A, A)
# Test types.MethodType
print types.MethodType
class C(object):
    def f(self):
        return 'hello world'
    def g(self, x, y):
        return x + y
c = C()
print c.f
print types.MethodType(c.f, c, C)
print c.g
print types.MethodType(c.g, c, C)
# Test types.UnboundMethodType
print types.UnboundMethodType
print types.UnboundMethodType(c.g, c, C
