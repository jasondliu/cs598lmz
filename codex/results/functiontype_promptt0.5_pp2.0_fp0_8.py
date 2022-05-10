import types
# Test types.FunctionType in a function.
def f():
    return types.FunctionType

print types.FunctionType
print f()
# Test types.FunctionType in a class.
class Foo:
    def f(self):
        return types.FunctionType

print Foo().f()()
# Test types.FunctionType in a function defined in a class.
class Foo:
    def f(self):
        def g():
            return types.FunctionType
        return g

print Foo().f()()
# Test types.FunctionType in a class method.
class Foo:
    def f(self):
        return types.FunctionType
    def g(self):
        return self.f

print Foo().g()()
# Test types.FunctionType in a class method defined in a class.
class Foo:
    def f(self):
        def g(self):
            return types.FunctionType
        return g
    def h(self):
        return self.f

print Foo().h()(None)
# Test types.MethodType in a function.
def f():
    return types.MethodType

