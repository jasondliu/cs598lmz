import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

class TestUnicodeReplace:
    def testErrorHandling(self):
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            data = b'\xff'
            self.assertEqual(data.decode(encoding, 'ignore'), '')
            self.assertEqual(data.decode(encoding, 'replace'),
                             data.decode(encoding, 'ignore').replace('\ufffd', '?'))
            self.assertRaises(UnicodeDecodeError, data.decode,
                              encoding, 'strict')
            try:
                data.decode(encoding, 'add_one_codepoint')
            except UnicodeDecodeError as x:
                self.assertEqual(x.object, data)
                self.assertEqual(x.start, 0)
                self.assertEqual(x.end, len(data))
            else:
                self.fail('UnicodeDecodeError not raised')

        # try to trigger a BufferError
        data = b'\x
