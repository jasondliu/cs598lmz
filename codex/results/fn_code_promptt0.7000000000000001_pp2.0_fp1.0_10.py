fn = lambda: None
# Test fn.__code__
fn.__code__ = Test(lambda : None)
# Test fn.__code__.co_args
fn.__code__.co_argcount = Test(1)
# Test fn.__code__.co_consts
fn.__code__.co_consts = Test((1, 2))
# Test fn.__code__.co_name
fn.__code__.co_name = Test("fn")

"""
class TestClass:
    "class TestClass"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "TestClass(%s, %s)" % (self.a, self.b)

TestClass(1, 2)
"""
TestClass = Test(type("TestClass", (), {
    "__init__": lambda self, a, b: (setattr(self, "a", a), setattr(self, "b", b)),
    "__repr__": lambda self: Test("TestClass(%s, %s)"
