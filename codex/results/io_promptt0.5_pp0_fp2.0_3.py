import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test___init__(self):
        # RawIOBase()
        self.assertEqual(str(io.RawIOBase()), '<_io.RawIOBase>')

    def test___init___override(self):
        # RawIOBase()
        class MyRawIOBase(io.RawIOBase):
            def __init__(self):
                self.name = 'MyRawIOBase'
        self.assertEqual(str(MyRawIOBase()), '<MyRawIOBase>')

    def test___init___override_no_name(self):
        # RawIOBase()
        class MyRawIOBase(io.RawIOBase):
            def __init__(self):
                pass
        self.assertEqual(str(MyRawIOBase()), '<_io.RawIOBase>')

    def test_close(self):
        # RawIOBase.close()
        class MyRawIOBase(io.RawIOBase):
            def close(self):
                self.name
