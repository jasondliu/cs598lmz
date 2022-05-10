import io
# Test io.RawIOBase.read()
try:
    io.RawIOBase.read()
except:
    # io.RawIOBase.read() raises NotImplementedError in this environment
    import unittest

    class TestCodecs(unittest.TestCase):
        def test_noop(self):
            self.assertTrue(True)

else:

    import codecs

    class TestCodecs(unittest.TestCase):
    #TODO:
    #  - test for correctness for hiencoding/hidescapes
    #  - check testable encodings
    #  - transform/sub codecs (?)

        def test_transform_leader(self):
            t = codecs.transform_leader(b'\x00\x01\x03')
            self.assertTrue(t(b'\x00\x01') == b'\x00\x01')
            self.assertTrue(t(b'\x02\x03') == b'\x00\x01\x02\x03')

