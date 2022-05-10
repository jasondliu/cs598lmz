fn = lambda: None
# Test fn.__code__ and fn.__defaults__
test_fn.__code__ = code
test_fn.__defaults__ = defaults
# Test a built-in function
assert inspect.isbuiltin(len)

# Test a class method
class AClass:
    def a_method(self):
        pass
assert inspect.ismethod(AClass.a_method)
assert inspect.isfunction(AClass.a_method)

# Test a static method
def a_static_method():
    pass
a_static_method = staticmethod(a_static_method)
assert inspect.isfunction(a_static_method)
assert not inspect.ismethod(a_static_method)

# Test a class
class TestClass:
    "Test doc string"
    def __init__(self):
        pass
    def method1(self, *args, **kwargs):
        pass
    def method2(self, *args):
        pass
print inspect.getdoc(TestClass)
print inspect.getdoc(TestClass.method1)
assert inspect.isclass(TestClass
