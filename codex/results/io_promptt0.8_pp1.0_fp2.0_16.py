import io
# Test io.RawIOBase from io
class TestRawIOBase(unittest.TestCase):
    def test_readable(self):
        self.assertIs(io.RawIOBase.readable(io.RawIOBase()), False)
    
    def test_writable(self):
        self.assertIs(io.RawIOBase.writable(io.RawIOBase()), False)
    
    def test_seekable(self):
        self.assertIs(io.RawIOBase.seekable(io.RawIOBase()), False)
    
    def test_readinto(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readinto(b'a')
    
    def test_readall(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readall()
    
    def test_readline(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readline()
    
    def test_readlines(self):
       
