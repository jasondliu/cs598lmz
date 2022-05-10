import io
# Test io.RawIOBase

import io

class IOBaseTest(unittest.TestCase):

    def test_attributes(self):
        rawio = io.RawIOBase()
        self.assertEqual(rawio.mode, 'x')
        self.assertEqual(rawio.name, '<uninitialized>')

    # XXX The following test is disabled, because it's unclear
    #     how to achieve the desired behaviour.
    #def test_readinto(self):
    #    # Make sure 'readinto' and 'write' don't share the same buffer
    #    buf = bytearray(2)
    #    rawio = io.RawIOBase()
    #    rawio.write(b'ab')
    #    rawio.seek(0)
    #    self.assertEqual(rawio.readinto1(buf), 2)
    #    self.assertEqual(buf, b'ab')
    #    rawio.seek(0)
    #    buf[0] = b'x'
    #    self.assertEqual(rawio
