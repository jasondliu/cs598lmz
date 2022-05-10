import io
# Test io.RawIOBase.

class RawIOBaseTest(unittest.TestCase):

    def test_attributes(self):
        # RawIOBase defines a number of attributes which *may* be accessed
        # via the base class, but which should not be set.
        # Some of them are read-only, others depend on the implementation
        # whether they should be read-only.
        class RawIOBaseSubclass(io.RawIOBase):
            pass
        rawio = RawIOBaseSubclass()
        rawio.close()
        rawio.closed
        rawio.mode
        rawio.name
        rawio.encoding
        rawio.newlines
        rawio.readinto
        rawio.seek
        rawio.write
        rawio.writelines


class BytesIOImplTestMixin:

    def test_read_from_closed_file(self):
        self.bio.close()
        self.assertRaises(ValueError, self.bio.read)

    def test_write_to_closed_file(self):
        self.bio.close
