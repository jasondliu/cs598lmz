import io
# Test io.RawIOBase properties
import io
import sys
import _io

modes = ['r', 'rb', 'rw', 'rwb', 'w+b', 'w+', 'a+', 'a+b']

def read_all(f):
    return f.readall()

def write_all(f, data):
    f.writeall(data)

def internal_buf_size(f):
    if 'r' in f.mode:
        return f.getbuffer().nbytes
    else:
        return f.buffer.nbytes

class TestIoRawIOBase(unittest.TestCase):
    def test_closed_property(self):
        # Test io.RawIOBase.closed property
        # Constructors
        for kwargs in [{}, {'a':1}, {'a':1, 'b':2}]:
            b = io.RawIOBase(**kwargs)
            self.assertEqual(b.closed, False)
            b.close()
            self.assertEqual(b.closed, True)
        # .close
