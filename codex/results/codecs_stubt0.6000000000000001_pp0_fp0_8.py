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

class TestDecodingMap(unittest.TestCase):
    def test_decoding_map(self):
        # make sure that the decoding map is correct
        for encoding in ('utf-8', 'utf-8-sig', 'utf-16', 'utf-16-be',
                         'utf-16-le', 'utf-32', 'utf-32-be', 'utf-32-le'):
            for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                           'add_utf16_bytes', 'add_utf32_bytes'):
                for bom in (False, True):
                    for prepend in (b'', b'\r', b'\r\r', b'\r\r\r',
                                    b'\r\n', b'\r\n\r\n'):
                        for append in (b'', b'\r', b'\r\r', b'\r\r\r',
                                       b'\r\n', b'\r\n\r\n'
