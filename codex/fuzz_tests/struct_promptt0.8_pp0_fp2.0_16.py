import _struct
# Test _struct.Struct
import _testcapi


# Issue #11278: test that Struct.unpack() always returns an iterable that
# supports len()
class IterNoLen:
    def __len__(self):
        raise Exception("my list object should not have been asked for its len()")
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration

class IterWithLen:
    def __len__(self):
        return 0
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration


import struct

class StructTest(unittest.TestCase):
    def test_unpack(self):
        for code, format, size in _testcapi._struct_alignment_testcases:
            st = struct.Struct(code + format)
            self.assertEqual(st.unpack(b"a"*size),
                             _testcapi._struct_alignment_test_result(code, size))

        self.assertEqual(struct.Struct("").
