import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'blah'

class Test(unittest.TestCase):
    def test_read(self):
        # This test passes if the read method is not called.
        self.assertEqual(b'blah', File().read())

if __name__ == '__main__':
    unittest.main()
</code>

