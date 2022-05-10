import types
# Test types.FunctionType
def f():
    pass

def g(a, b):
    return a + b

def h(a, b=1, *pos, **kw):
    return a + b

def i(a, b):
    yield a + b

def j(a, b):
    yield from a + b

def k(*args, **kw):
    pass

def l(a, b):
    """function doc"""
    pass

# Should not be detected as a function
class C:
    def m(self):
        pass

class D(C):
    pass

def n(a:int=42) -> str:
    pass

def o(a:'foo'=42) -> 'bar':
    pass

# Test types.BuiltinFunctionType
lst = [1, 2, 3]
lst.append(4)

# Test types.MethodType
class E:
    def __init__(self, val):
        self.val = val
    def f(self):
        return self.val

e = E(
