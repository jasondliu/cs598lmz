import types
# Test types.FunctionType

class TestFuncType:
    def f1(x):
        pass

    lambda x: None

    class C:
        def f2(self, x):
            pass

        def f3(self, x=1):
            pass

    class D(C):
        def f2(self, x, y):
            pass

        def f3(self, x=1, y=2):
            pass

    try:
        f1.__code__.co_flags |= inspect.CO_VARARGS
    except TypeError:
        pass  # Can't set CO_VARARGS

    try:
        f1.__code__.co_flags |= inspect.CO_VARKEYWORDS
    except TypeError:
        pass  # Can't set CO_VARKEYWORDS

    def test_function_type(self):
        assert inspect.isfunction(self.f1)
        assert inspect.isfunction(self.C.f2)
        assert inspect.isfunction(self.C.f3)
        assert inspect.isfunction(
