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
    # test surrogatepass
    for encoding in ('utf-16', 'utf-32'):
        for errors in ('surrogatepass', 'surrogateescape'):
            for input in ('\udc00', '\ud800\udc00'):
                for output in ('\udc00', '\ud800\udc00'):
                    for input_encoding in ('utf-16', 'utf-32'):
                        for output_encoding in ('utf-16', 'utf-32'):
                            if input_encoding == output_encoding:
                                continue
                            print(encoding, errors, input, output, input_encoding, output_encoding)
                            try:
                                codecs.decode(input.encode(input_encoding), encoding, errors)
                            except UnicodeDecodeError:
                                pass
                            else:
                                raise AssertionError("should have raised")
                            try:
                                codecs.encode(output, encoding, errors)
                            except UnicodeEncode
