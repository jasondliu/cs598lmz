import types
# Test types.FunctionType

def f(): pass

print type(f) == types.FunctionType # True - f is a function

print isinstance(f, types.FunctionType) # True - same as above

# Test types.LambdaType

g = lambda x: x + 1

print type(g) == types.LambdaType # True

# Test types.ClassType

class FooClass:
  "foo"
fooInstance = FooClass()

print type(FooClass) == types.ClassType # True

print type(fooInstance) == types.InstanceType # True

print isinstance(FooClass(), FooClass) # True

print isinstance(fooInstance, FooClass) # True

# Test types.MethodType

class Dummy:
    def __init__(self):
        self.x = "bar"
    def foo(self):
        return self.x

dummyInst = Dummy()
foo = dummyInst.foo

print type(foo) == types.MethodType # True

print isinstance(foo, types.MethodType) #
