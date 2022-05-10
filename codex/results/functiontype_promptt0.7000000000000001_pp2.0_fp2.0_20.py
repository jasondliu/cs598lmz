import types
# Test types.FunctionType
def func1():
    pass
print(isinstance(func1, types.FunctionType))
print(isinstance(func1, types.BuiltinFunctionType))
print(isinstance(len, types.BuiltinFunctionType))
# Test types.MethodType
def func2(self, name):
    print('Hello %s' % name)
    print(self, id(self))
def func3(self, name):
    print('Hi %s' % name)
    print(self, id(self))
class A:
    def __init__(self):
        self.name = 'Alice'
        self.method = types.MethodType(func2, self)
        self.method2 = types.MethodType(func3, self)
a = A()
a.method('Bob')
a.method2('Bob')
# Test types.LambdaType
f = lambda x: x * x
print(isinstance(f, types.LambdaType))
# Test types.GeneratorType
def gen():
    print('start')
    yield 1
    print('continue
