import types
# Test types.FunctionType
def func(x):
    return x

print(type(func))

# Test types.LambdaType
lamb = lambda x: x

print(type(lamb))

# Test types.GeneratorType
def gen(x):
    for i in range(x):
        yield i

print(type(gen))

# Test types.MethodType
class A:
    def __init__(self):
        self.x = 1
    
    def method(self):
        pass

a = A()
print(type(a.method))

# Test types.BuiltinMethodType
print(type(list.append))

# Test types.BuiltinFunctionType
print(type(len))

# Test types.ModuleType
import types
print(type(types))

# Test types.TracebackType
def f():
    try:
        raise Exception
    except Exception:
        import sys
        return sys.exc_info()[2]

print(type(f()))

# Test types.FrameType
def f():

