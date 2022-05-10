import types
# Test types.FunctionType is function on any platform"""
from types import FunctionType
from .test_importlib.builtin import BuiltinTestCase


class TestErrorClasses(BuiltinTestCase):


    def test_error_classes(self):
        self.assertTypeEqual(ImportError, type)
        self.assertTypeEqual(ModuleNotFoundError, type)

    def test_bad_magic_error(self):
        exc = BadMagicError(b'bad magic', b'name', 'path')
        self.assertEqual(str(exc), "bad magic number in 'name': b'bad magic'")
        self.assertEqual(exc.name, b'name')
        self.assertEqual(exc.path, 'path')
        self.assertIsInstance(exc, ImportError)
        exc = BadMagicError(b'bad magic', u'na\N{SNOWMAN}me', '\u1234')
        self.assertEqual(str(exc),
             u"bad magic number in 'na\N{SNOWMAN}me': b'bad magic'")
       
