import io
# Test io.RawIOBase(io.BytesIO)
class RawIOBase_BytesIO_Test(unittest.TestCase):
    def test_RawIOBase_BytesIO_Test(self):
        r = io.RawIOBase(io.BytesIO())
        r.close()
        r.flush()
        r.fileno()
        r.isatty()
        r.read()
        r.readable()
        r.readline()
        r.readlines()
        r.seek(0,0)
        r.seekable()
        r.tell()
        r.truncate()
        r.writable()
        r.write(b'')
        r.writelines([b''])

if __name__ == "__main__":
    unittest.main()
