import mmap
# Test mmap.mmap functionality by reading all lines into memory, then modifying,
# then writing to a temporary file.
import tempfile

class TestMmap(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.fname = tempfile.mktemp()
        text = b"0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n"
        with open(self.fname, 'wb') as fobj:
            fobj.write(text)

        self.m = mmap.mmap(fobj.fileno(), 0, access=mmap.ACCESS_WRITE)

    def tearDown(self):
        self.m.close()
        os.remove(self.fname)
        super().tearDown()

    def test_fixed_addresses(self):
        # Make sure mmap.mmap objects have a fixed address, similar to a
        # bytes object.
        m1 = mmap.mmap(-1, 1024)
