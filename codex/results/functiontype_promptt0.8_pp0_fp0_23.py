import types
# Test types.FunctionType and types.MethodType:
def test_function():
    return "Hello world!"
def test_function_args(a=0, b=1):
    return a + b

class Foo:
    def __init__(self):
        self._arg = 0
    def test_method(self):
        return "Hello world!"
    def test_method_args(self, a=0, b=1):
        return self._arg + a + b

def test_types():
    print("Checking types.FunctionType...")
    assert(type(test_function) == types.FunctionType)
    assert(type(test_function_args) == types.FunctionType)
    assert(type(Foo.test_method) == types.MethodType)
    assert(type(Foo.test_method_args) == types.MethodType)
    f = Foo()
    assert(type(f.test_method) == types.MethodType)
    assert(type(f.test_method_args) == types.MethodType)
    try:
        assert(type(lambda
