import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_error_conditions(self):
        # should not allow instantiation
        self.assertRaises(TypeError, io.RawIOBase)
        # should not allow instantiation of a subclass without implementing read
        class MyRawIO(io.RawIOBase):
            pass
        self.assertRaises(TypeError, MyRawIO)
        # should not allow instantiation of a subclass without implementing write
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b''
        self.assertRaises(TypeError, MyRawIO)
        # should not allow instantiation of a subclass without implementing fileno
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b''
            def write(self, b):
                return 0
        self.assertRaises(TypeError, MyRawIO)
        # should not allow instantiation of a subclass without implementing readable
        class MyRawIO(io.RawIOBase):
           
