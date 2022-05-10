import bz2
bz2c = bz2.BZ2Compressor()

def bz2_writer(writer):
    def _writer(data):
        writer.write(bz2c.compress(data))
    return _writer

def bz2_close(writer):
    writer.write(bz2c.flush())
    writer.close()

def bz2_reader(reader):
    return bz2.BZ2Decompressor(reader)

def bz2_open(filename, mode='r'):
    if mode == 'r':
        return bz2_reader(open(filename, 'rb'))
    elif mode == 'w':
        return bz2_writer(open(filename, 'wb'))
    else:
        raise IOError("Mode not supported")

class TestBz2(TestCase):
    def test_bz2(self):
        self.assertEqual(bz2_reader(bz2_writer(BytesIO())).read(), b"")
        data = b"this is a test"
        b
