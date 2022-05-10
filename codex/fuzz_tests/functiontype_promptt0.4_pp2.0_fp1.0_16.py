import types
# Test types.FunctionType
def func0(): pass
func1 = lambda: None
def func2(x): return x
def func3(x, y): return x + y
def func4(x, y, z): return x + y + z
class A(object):
    def __init__(self): pass
    def func5(self): pass
    def func6(self, x): return x
    def func7(self, x, y): return x + y
    def func8(self, x, y, z): return x + y + z
a = A()

for f in [func0, func1, func2, func3, func4, a.func5, a.func6, a.func7, a.func8]:
    print(type(f), isinstance(f, types.FunctionType))

# Test types.LambdaType
l0 = lambda: None
l1 = lambda x: x
l2 = lambda x, y: x + y
l3 = lambda x, y, z: x + y + z

for l in [l0, l1, l
