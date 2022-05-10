import types
# Test types.FunctionType
def f(x):
    return x

def g(x):
    def h(y):
        return x + y
    return h

class A:
    def __init__(self, x):
        self.x = x
    def f(self, y):
        return self.x + y

a = A(42)

# Test type constructor
if types.FunctionType(f.func_code, f.func_globals, 'newname', f.func_defaults, f.func_closure) is not f:
    raise TestFailed
if types.FunctionType(g(f).func_code, g(f).func_globals, 'newname', g(f).func_defaults, g(f).func_closure)()(2) != 3:
    raise TestFailed
if types.FunctionType(a.f.im_func.func_code, a.f.im_func.func_globals, 'newname', a.f.im_func.func_defaults, a.f.im_func.func_
