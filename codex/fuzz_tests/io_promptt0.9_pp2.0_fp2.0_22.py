import io
# Test io.RawIOBase

class BaseTestIO(unittest.TestCase):

    # RawIOBase is an abstract class; subclasses must override read().  So
    # start off by just making sure that it can be instantiated.

    def test_init(self):
        Support.import_module('io')
        rawio = io.RawIOBase()
        Support.import_module('_io')
        rawio = _io.BufferedIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, b'')
        self.assertRaises(io.UnsupportedOperation, rawio.write, b'1')
        self.assertRaises(io.UnsupportedOperation, rawio.seek, 0)
        self.assertRaises(io.UnsupportedOperation, rawio.tell)
        self.assertRaises(io.UnsupportedOperation, rawio.truncate, 0)

    @support.cpython_only
    def test_subclass(self):
        class MyRaw
