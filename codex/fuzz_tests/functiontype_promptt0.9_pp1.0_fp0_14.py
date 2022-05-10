import types
# Test types.FunctionType
def foo():
    pass
str_type = type('str')
if not type(foo) is types.FunctionType:
    raise RuntimeError('type(foo) is not types.FunctionType')
if type(dir) is not types.FunctionType:
    raise RuntimeError('type(dir) is not types.FunctionType')
if type(str_type) is types.FunctionType:
    raise RuntimeError('type(str_type) is types.FunctionType')


# Test types.GeneratorType
foo_gen = (x for x in range(10) if x % 2 == 1)
if not type(x) is types.GeneratorType:
    raise RuntimeError('type(x) is not types.GeneratorType')


import unittest

class TestGeneratorTypes(unittest.TestCase):

    def test_isinstance_generator(self):
        def xrange(x):
            for i in range(x):
                yield i

        x = xrange(10)
        self.assertTrue(isinstance(x, types.GeneratorType))
        self
