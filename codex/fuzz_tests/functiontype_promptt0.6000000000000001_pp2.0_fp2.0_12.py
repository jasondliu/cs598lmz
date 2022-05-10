import types
# Test types.FunctionType without a name
class C:
    def __init__(self):
        self.f = types.FunctionType(lambda: None, globals())

# Test types.FunctionType with a name
class D:
    def __init__(self):
        self.f = types.FunctionType(lambda: None, globals(), "foo")

# Test types.FunctionType with a docstring
class E:
    def __init__(self):
        self.f = types.FunctionType(lambda: None, globals(), "foo", "bar")

# Test types.FunctionType with a closure
def f(x):
    def g(y):
        return x + y
    return g
class F:
    def __init__(self):
        self.f = f(3)

# Test types.LambdaType
class G:
    def __init__(self):
        self.f = types.LambdaType(lambda: None, globals())

# Test types.LambdaType with a docstring
class H:
    def __init__(self):
