import types
types.new_module('numpy')
import numpy
numpy.__name__ = 'numpy'

class NumpyTestCase(unittest.TestCase):

    def assertArrayEqual(self, x, y, *args, **kwargs):
        unittest.TestCase.assertTrue(self, (x == y).all(), *args, **kwargs)

    def assertArrayLess(self, x, y, *args, **kwargs):
        unittest.TestCase.assertTrue(self, (x < y).all(), *args, **kwargs)

    def assertWarns(self, func, category=None, message=None, regexp=None):
        assert regexp is None, "Regexp is not supported"
        warnings_manager = WarningsManager()
        warnings.simplefilter('always')
        with warnings_manager:
            func()
        self.assertTrue(warnings_manager.warnings)
