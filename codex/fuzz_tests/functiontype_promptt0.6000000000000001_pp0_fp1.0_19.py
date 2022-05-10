import types
# Test types.FunctionType
def f(): pass
def g(): pass
f.__name__ = 'f'
g.__name__ = 'g'
print(type(f)==types.FunctionType)
print(type(g)==types.FunctionType)
print(type(f)==types.BuiltinFunctionType)
print(type(g)==types.BuiltinFunctionType)
print(f.__name__)
print(g.__name__)

print("==========")
# Test types.LambdaType
lf = lambda : None
lg = lambda x, y=1: x+y
print(type(lf)==types.LambdaType)
print(type(lg)==types.LambdaType)
print(type(lf)==types.FunctionType)
print(type(lg)==types.FunctionType)

print("==========")
# Test types.MethodType
class A:
    def f(self):
        pass
    def g(self):
        pass
    def h(self):
        pass
a = A()
print(type
