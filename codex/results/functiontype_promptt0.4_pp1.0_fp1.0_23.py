import types
# Test types.FunctionType
def foo():
    return 1

def bar():
    return 2

def baz():
    return 3

print(type(foo))
print(type(bar))
print(type(baz))

print(isinstance(foo, types.FunctionType))
print(isinstance(bar, types.FunctionType))
print(isinstance(baz, types.FunctionType))

# Test types.BuiltinFunctionType
print(isinstance(print, types.BuiltinFunctionType))
print(isinstance(foo, types.BuiltinFunctionType))

# Test types.MethodType
class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4

    def foo(self):
        return self.a

    def bar(self):
        return self.b

    def baz(self):
        return self.c

obj = MyClass()

print(isinstance(obj.foo, types.MethodType))
print(isinstance(obj.bar, types
