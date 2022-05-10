from types import FunctionType
list(FunctionType(list(FunctionType([], list([]))), {}))
"""
    self.assertCodeExecution(code)


class BuiltinFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["__init__", "__new__"]

    not_implemented = [
        'test_class',
        'test_complex',
        'test_frozenset',
    ]
