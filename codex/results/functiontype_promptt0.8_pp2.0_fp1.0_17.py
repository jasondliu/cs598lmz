import types
# Test types.FunctionType, types.GeneratorType

def fun0():
    yield

def fun1(): pass

def fun2(x):
    yield x

def fun3(x,y):
    return x

class A:
    def fun4(self, x):
        yield x

a = A()
a.fun4(4)

print types.FunctionType(fun0, globals())
