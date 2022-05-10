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
    # Codec lookup
    for encoding in ('ascii', 'iso-8859-1', 'iso8859-1',
                     'latin-1', 'latin1', 'cp819', 'latin-2',
                     'latin2', 'iso-8859-2', 'iso8859-2',
                     'latin-3', 'latin3', 'iso-8859-3', 'iso8859-3',
                     'latin-4', 'latin4', 'iso-8859-4', 'iso8859-4',
                     'latin-5', 'latin5', 'iso-8859-9', 'iso8859-9',
                     'latin-6', 'latin6', 'iso-8859-10', 'iso8859-10',
                     'latin-7', 'latin7', 'iso-8859-13', 'iso8859-13',
                     'latin-8', 'latin8', 'iso-8859-14', 'iso8859-14',
                     'l
