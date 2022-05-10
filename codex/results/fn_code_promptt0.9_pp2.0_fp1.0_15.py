fn = lambda: None
# Test fn.__code__ is not inspected for parameter annotations. Python 3
# does not define __code__ for regex matched strings.
@p(1)
def fn_legacy():
    pass


class TestCase(unittest.TestCase):

    def test_argument_types(self):
        pass

    def test_argument_default(self):
        pass

    def test_class_annotation(self):
        pass

    def test_varargs(self):
        pass

    def test_kwargs(self):
        pass

    def test_return_types(self):
        pass

    def test_return_annotation(self):
        pass

    def test_method_types(self):
        pass

    def test_method_annotation(self):
        pass

    def test_static_method_types(self):
        pass

    def test_static_method_annotation(self):
        pass

    def test_class_method_types(self):
        pass

    def test_class_method_annotation(self):
        pass

    def test_module_level_types(
