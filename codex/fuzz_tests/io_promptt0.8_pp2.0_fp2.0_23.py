import io
# Test io.RawIOBase
class TestRawIOBase(TestIOBase):
    def test_rawiobase_flush(self):
        # RawIOBase.flush()
        with mock.patch.object(io.RawIOBase, 'flush',
                               return_value=None) as mock_flush:
            r = io.RawIOBase()
            self.assertIsNone(r.flush())
            self.assertIsNone(r.flush())
            expected = [mock.call(), mock.call()]
            self.assertEqual(expected, mock_flush.call_args_list)

    def test_rawiobase_read(self):
        # RawIOBase.read([size])
        # A test may override this with a more specific test.
        with mock.patch.object(io.RawIOBase, 'read',
                               return_value=b'') as mock_read:
            r = io.RawIOBase()
            self.assertEqual(b'', r.read())
            self.assertEqual(b'', r.read(0))
            self.assertE
