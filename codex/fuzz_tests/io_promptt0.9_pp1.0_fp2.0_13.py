import io
# Test io.RawIOBase and assert that it works as we expect
class TestRawIOBase(unittest.TestCase):
  def testReadAtLeastOnce(self):
    class MockRawIO(io.RawIOBase):
      def readinto(self, buffer):
        if not hasattr(self, 'buffer'):
          self.buffer = b'test'
        if not self.buffer:
          return 0
        buffer[0:len(self.buffer)] = self.buffer
        self.buffer = self.buffer[len(self.buffer):]
        return len(buffer)
    buf = bytearray(10)
    io2 = MockRawIO()
    self.assertEqual(io2.readinto(buf), 4)
    self.assertEqual(buf, bytearray(b'test'))
    self.assertEqual(io2.readinto(buf), 4)
    self.assertEqual(buf, bytearray(b'test'))
    self.assertEqual(io2.readinto(buf), 0)
    self.assertEqual(buf
