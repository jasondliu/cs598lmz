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

def test_main():
    def test(encoding):
        decoder = codecs.getincrementaldecoder(encoding)()
        decoder.setstate((0,1))
        test_data = [
            'QWxhZGRpbjpvcGVuIHNlc2FtZQ==\\n'.encode(encoding),
            'PSJceDUwMFsxMzddIj4=\\n'.encode(encoding),
            'PyAoT0hFUkFURVMpXHg1MDBbMTM3XTo=\\n'.encode(encoding),
            'IGJhc2U2NC5kZWNvZGUoKVx4NTAwWzEzN109\\n'.encode(encoding),
            'PT4gJ09IRVJBVEVTJ1x4NTAwWzEzN10nXHg1MDBbMTM3XiosXHg1MDBbMTM3XVtyZXR1cm5dXHg1M
