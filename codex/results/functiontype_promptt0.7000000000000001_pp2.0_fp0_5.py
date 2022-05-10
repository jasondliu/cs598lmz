import types
# Test types.FunctionType
# Same as the previous test, but now with the code object replaced
# by a function object (types.FunctionType).
def f(x) : return x
def g(x) : return x

class A(Exception):
    pass

def foo():
    try:
        raise A()
    except A, o:
        o.__class__ = types.FunctionType
        o(3)

try:
    foo()
except TypeError:
    pass
else:
    raise RuntimeError, "Should have raised a TypeError"

# another one
def h(x) : return x
class B(Exception):
    pass

def foo2():
    try:
        raise B()
    except B, o:
        o.__class__ = types.FunctionType
        o(3)

try:
    foo2()
except TypeError:
    pass
else:
    raise RuntimeError, "Should have raised a TypeError"

# another one
def i(x) : return x
class C(Exception):
    pass

def foo3():
   
