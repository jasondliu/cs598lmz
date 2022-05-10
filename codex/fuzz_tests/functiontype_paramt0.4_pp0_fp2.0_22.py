from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# pytest.mark.parametrize

# pytest.mark.parametrize
class TestClass(object):
    @pytest.mark.parametrize("test_input,expected", [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 42),
    ])
    def test_eval(self, test_input, expected):
        assert eval(test_input) == expected


# pytest.mark.parametrize
class TestClass(object):
    @pytest.mark.parametrize("x", [0, 1])
    @pytest.mark.parametrize("y", [2, 3])
    def test_foo(self, x, y):
        pass


# pytest.mark.parametrize
class TestClass(object):
    @pytest.mark.parametrize(("x", "y"), [(0, 2), (1, 3)])
    def test_foo(self, x, y):
