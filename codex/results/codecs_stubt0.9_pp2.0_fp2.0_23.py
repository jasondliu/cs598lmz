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

encodings = [
    # charset output ascii/unicode input (normal tests don't test unicode-input)
    # the multiple entries for UTF-7 are to test multi-byte behavior
    ("ascii", ['abc'], 'abc'),
    ("ascii", [u'abc'], 'abc'),
    ("latin1", ['abc'], 'abc'),
    ("latin1", [u'abc'], 'abc'),
    ("utf-8", ['abc'], 'abc'),
    ("utf-8", [u'abc'], 'abc'),
    ("utf-8", [u'\u20ac'], '\xe2\x82\xac'),
    ("mbcs", ['abc'], 'abc'),
    #("oem", ['abc'], 'abc'), # hangs on windows
    #("utf-7", ['+ABIAA-'], 'abc'),
    #("utf-7", ['+ABIAA-'], u'abc'),
    #("utf-7", [u'+ABIAA-'], 'abc'),
   
