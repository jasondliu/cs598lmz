import types
# Test types.FunctionType
def func():
    pass

print(type(func))
print(type(len))

# types.LambdaType
print(type(lambda x: x))
# types.GeneratorType
print(type((x for x in range(10))))
# types.BuiltinFunctionType
print(type(len))
# types.BuiltinMethodType
print(type([].append))
# types.MethodType
class Foo:
    def func(self):
        pass

f = Foo()
print(type(f.func))

# types.ModuleType
import sys
print(type(sys))

# types.TracebackType
try:
    1/0
except Exception as e:
    print(type(e.__traceback__))

# types.FrameType
def bar():
    return bar.__code__.__class__

print(type(bar()))

# types.CodeType
def foo():
    pass

print(type(foo.__code__))

# types.GetSetDescriptorType
class A:
   
