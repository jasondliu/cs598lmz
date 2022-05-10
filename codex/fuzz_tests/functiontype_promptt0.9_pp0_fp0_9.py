import types
# Test types.FunctionType
def f():
  print('This a function')
print(type(f))
print(type(f)==types.FunctionType)
# Test types.LambdaType
x=lambda a,b,c:a+b+c
print(type(x))
print(type(x)==types.LambdaType)
# Test types.GeneratorType
def fib(n):
  a,b=0,1
  for i in range(n):
    a,b=b,a+b
    yield a
y=fib(10)
print(type(y))
print(type(y)==types.GeneratorType)
# Test types.BuiltinFunctionType
print(type(abs))
print(type(abs)==types.BuiltinFunctionType)
# Test types.BuiltinMethodType
print(type(x.__lt__))
print(type(x.__lt__)==types.BuiltinMethodType)
# Test types.MethodType
class S:
  def m(self, x, y):
    return x+y
z=
