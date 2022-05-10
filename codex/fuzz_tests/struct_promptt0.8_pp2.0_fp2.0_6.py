import _struct
# Test _struct.Struct's 's' format over large data
import struct
from test.support import run_unittest


class StructS(unittest.TestCase):

    def test_struct_s(self):
        # 's' format over large data
        for i in (1,  # 1-byte buffer
            10,  # ascii
            1024):  # non-ascii
            buf = struct.pack('i', i) + b'x' * i
            data = struct.unpack('i', buf[:struct.calcsize('i')])[0]
            st = _struct.Struct('i')
            v = st.unpack_from(buf)
            self.assertEqual(v, data)


if __name__ == '__main__':
    run_unittest(StructS)
