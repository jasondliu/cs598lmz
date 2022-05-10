import types
# Test types.FunctionType
# Test types.LambdaType
# Test types.GeneratorType

# Test each of the objects in the module, by importing them and running them

# make sure the module imports without error.
import test_types

def f():
    return 1

class G:
    def __init__(self):
        pass
    def __call__(self, x, y, z=3):
        return x + y + z

g = G()

class X:
    def __init__(self):
        pass
    def g(self, x, y, z=3):
        return x + y + z

x = X()

class Y(X):
    def __init__(self):
        X.__init__(self)
    def f(self):
        return 2
    def g(self, a, b, c=4):
        return X.g(self, a, b, c=c)

y = Y()

class Z(Y):
    def __init__(self):
        Y.__init__(self)
