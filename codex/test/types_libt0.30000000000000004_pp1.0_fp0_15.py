import types
types.ClassType = types.TypeType

import unittest
from test import test_support

class TestCase(unittest.TestCase):

    def test_import_star(self):
        # This will import * from test_import.
        from test import test_import_star
        self.assert_(test_import_star.__all__ is None)
        self.assert_(test_import_star.__author__ == "Nobody")
        self.assert_(test_import_star.__doc__ is None)
        self.assert_(test_import_star.__file__ == __file__.replace('\\', '/'))
        self.assert_(test_import_star.__name__ == "test_import_star")
        self.assert_(test_import_star.__package__ == "test")
        self.assert_(test_import_star.__path__ == [__path__[0].replace('\\', '/')])
        self.assert_(test_import_star.__version__ == "0.0.0")
