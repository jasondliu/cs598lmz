import types
# Test types.FunctionType
import unittest

class TestFunctionType(unittest.TestCase):

    def test_types(self):
        self.assertTrue(isinstance(lambda x: x, types.FunctionType))
        self.assertTrue(isinstance(lambda x, y=None: x, types.FunctionType))
        self.assertTrue(isinstance(lambda *args: args[0], types.FunctionType))
        self.assertTrue(isinstance(lambda **kw: kw['a'], types.FunctionType))
        self.assertTrue(isinstance(lambda *a,b: b, types.FunctionType))
        self.assertTrue(isinstance(lambda *a,b,**kw: b, types.FunctionType))
        self.assertTrue(isinstance(lambda a,b,*c,d,**kw: b, types.FunctionType))
        self.assertTrue(isinstance(lambda *a,b,c=1,**kw: b, types.FunctionType))
        self.assertTrue(isinstance(lambda *a,b,*c,d=1,**kw:
