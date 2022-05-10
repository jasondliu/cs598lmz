import io
# Test io.RawIOBase.readall

class RawIOTest(unittest.TestCase):
    def test_readall(self):
        self.assertEqual(io.RawIOBase().readall(), b'')

        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                self.pos += n
                return b"S"*n

            def seekable(self):
                return True

            def seek(self, pos, whence=io.SEEK_SET):
                if whence == io.SEEK_SET:
                    self.pos = pos
                elif whence == io.SEEK_CUR:
                    self.pos += pos
                else:
                    raise NotImplementedError
                return self.pos

            def readable(self):
                return True

        def get_raw(fn):
            return fn(MyRawIO())
        self.assertEqual(get_raw(lambda raw: raw.readall(10)), b"SSSSSSSSSS")
        self.assertEqual(get_raw(lambda raw: raw.readall()
