import _struct
# Test _struct.Struct on big-endian architectures
from test import test_struct
test_struct.bigendian = True
from test.test_struct import BigEndianStructTest
from test.test_struct import BigEndianStructTestWithFloat
from test.test_struct import BigEndianStructTestWithoutFloat
from test.test_struct import TestFormat
from test.test_struct import TestStruct
from test.test_struct import TestStructWithFloat
from test.test_struct import TestStructWithoutFloat
from test.test_struct import unpack


class BigEndianTestFormat(TestFormat):
    def test_native_size(self):
        self.assertEqual(self.struct.size, self.size)

    def test_native_alignment(self):
        self.assertEqual(self.struct.alignment, self.alignment)


class BigEndianTestStruct(TestStruct):
    pass


class BigEndianTestStructWithFloat(TestStructWithFloat):
    pass


class BigEndianTestStructWithoutFloat(TestStructWithoutFloat):
    pass


