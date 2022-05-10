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

class ContextDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(self, input, errors, final):
        self.decode_state = [final, errors]
        return codecs.utf_8_decode(input, errors, final)


def test_main():
    import sys
    BOM = b'\xef\xbb\xbf'
    BOM_LE = b'\xff\xfe'
    BOM_BE = b'\xfe\xff'
    BOM_UTF32_LE = b'\xff\xfe\x00\x00'
    BOM_UTF32_BE = b'\x00\x00\xfe\xff'
    UTF8_DATA = 't\xe9st.txt'
    UTF8_BOM_DATA = BOM + UTF8_DATA.encode('utf-8')
    UTF16_DATA = '\xff\xfe' + 't\x00\xe9\x00s\x00t\x00.\x00t\
