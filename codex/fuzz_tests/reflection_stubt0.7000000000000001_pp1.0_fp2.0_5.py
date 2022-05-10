fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
""")

    def test_code_object_2(self):
        self.assertCodeExecution("""
def fn():
    yield
fn.__code__ = fn.__code__
fn()
""")


class UnaryFloatOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'float'


class BinaryFloatOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'float'

    not_implemented = [
        'test_add_class',
        'test_add_complex',
        'test_add_frozenset',

        'test_and_bool',
        'test_and_bytearray',
        'test_and_bytes',
        'test_and_class',
        'test_and_complex',
        'test_and_dict',
        'test_and_float',
        'test_and_frozenset',
        'test_and_int',
        'test_and_list',
        '
