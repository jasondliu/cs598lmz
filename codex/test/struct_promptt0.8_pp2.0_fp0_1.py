import _struct
# Test _struct.Struct() and module level functions
#
import unittest
class StructTest(unittest.TestCase):
    def test_issue_5609(self):
        # Issue 5609: ensure Struct() makes its internal format string cache
        # weak-keyed
        class DictLike(object):
            def __getitem__(self, key):
                return 0
        class MyStruct(object):
            def __init__(self, fmt):
                self.struct = _struct.Struct(fmt)
            def pack(self, *args, **kwargs):
                return self.struct.pack(*args, **kwargs)
        d = DictLike()
        x = MyStruct('>i')
        d[d] = x
        x.pack(1)
        import gc
        gc.collect()
        d[d].pack(1)
    def test_unsigned_format(self):
        # Issue #15635: 'u' and 'I' parsed as unsigned integers.
        self.assertEqual(_struct.calcsize('u'), calcsize('L'))
