import types
# Test types.FunctionType
def func(x, y, z=1):
    return x + y + z

class A:
    pass

inst = A()

def func2(self, x,y):
   return "hello"

setattr(A, 'meth', func2)
# the following line will fail
setattr(inst, 'x', 1)
def sfunc(self):
    return 'world'

setattr(A, 'smeth', types.MethodType(sfunc, None, A))

# Test that default arguments are part of the function attributes
def f(x, y=1):
    return x * y

def f2(x=1, y=2):
    return x * y

# Test that default arguments are part of the function attributes
# but code object is not
def f3(x, y=1, z=2):
    return x * y

# Test keyword args (code object is not)
def f4(x, y=1, **z):
    return x * y

# Test keyword only args (code object is not)
