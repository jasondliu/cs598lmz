fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
"""
        self.assertCodeExecution(code)

    def test_code_set_code_object(self):
        code = """
fn = lambda: None
co = fn.__code__
fn.__code__ = co
"""
        self.assertCodeExecution(code)

    def test_code_set_code_object_bad_type(self):
        code = """
fn = lambda: None
co = fn.__code__
fn.__code__ = 1
"""
        self.assertCodeExecution(code)

    def test_code_set_code_object_bad_type_2(self):
        code = """
fn = lambda: None
co = fn.__code__
fn.__code__ = 'bad'
"""
        self.assertCodeExecution(code)


class BuiltinCodeFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["code"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',

