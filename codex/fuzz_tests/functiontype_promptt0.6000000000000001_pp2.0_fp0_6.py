import types
# Test types.FunctionType
class test_FunctionType:
    def test_FunctionType(self):
        def f():
            pass
        assert type(f) is types.FunctionType

    def test_FunctionType_with_default_args(self):
        def f(a=1):
            pass
        assert type(f) is types.FunctionType

    def test_FunctionType_with_varargs(self):
        def f(*args):
            pass
        assert type(f) is types.FunctionType

    def test_FunctionType_with_kwargs(self):
        def f(**kwargs):
            pass
        assert type(f) is types.FunctionType

    def test_FunctionType_with_varargs_and_kwargs(self):
        def f(*args, **kwargs):
            pass
        assert type(f) is types.FunctionType

    def test_FunctionType_with_annotations(self):
        def f(a: int):
            pass
        assert type(f) is types.FunctionType

    def test_FunctionType_with_annotations_and_default_
