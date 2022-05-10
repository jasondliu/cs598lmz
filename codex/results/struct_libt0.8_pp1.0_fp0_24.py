import _struct
import _testcapi

# Helper to check if we are running on a platform that uses different
# code for unicode literals, see issue #4106.
IS_SOURCE = '_testcapi' in _testcapi.__file__

class ModuleTests(unittest.TestCase):

    def test_forwards(self):
        # test internal struct members are accessible
        struct.error is _struct.error
        struct.Struct is _struct.Struct
        struct.unpack is _struct.unpack
        struct.pack is _struct.pack
        struct.pack_into is _struct.pack_into
        struct.unpack_from is _struct.unpack_from
        self.assertTrue(struct.calcsize("=hi") == _struct.calcsize("=hi"))
        self.assertTrue(struct.Struct("=hi") == _struct.Struct("=hi"))

    def test_unsupported_type(self):
        with self.assertRaises(TypeError) as e:
            struct.calcsize(b"<T")
       
