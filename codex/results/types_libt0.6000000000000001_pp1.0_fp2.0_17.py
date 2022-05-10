import types
types.FunctionType

# built-in functions
type(len)
types.BuiltinFunctionType

# built-in methods
type(__builtins__.len)
types.MethodType

# user-defined functions
def f():
    pass

type(f)
types.FunctionType

# user-defined methods
class C:
    def m(self):
        pass

type(C.m)
types.MethodType

# classes
type(C)
types.ClassType

# instances
type(C())
C

# generator functions
def g():
    yield 1

type(g)
types.GeneratorType

# generator objects
g = (x for x in range(3))
type(g)
types.GeneratorType

# other objects
type(object())
type(NotImplemented)
type(...
