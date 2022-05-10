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

test_decode_error = """
>>> '\x80'.decode('utf8', 'replace')
u'\\ufffd'
>>> '\x80'.decode('utf8', 'ignore')
u''
>>> '\x80'.decode('utf8', 'backslashreplace')
u'\\\\x80'
>>> '\x80'.decode('utf8', 'xmlcharrefreplace')
u'&#x80;'
>>> '\x80'.decode('utf8', 'add_one_codepoint')
u'a'
>>> '\x80'.decode('utf8', 'add_utf16_bytes')
u'ab'
>>> '\x80'.decode('utf8', 'add_utf32_bytes')
u'abcd'

>>> '\x80'.decode('iso-8859-1', 'replace')
u'\\ufffd'
>>> '\x80'.decode('iso-8859-1', 'ignore')
u''
>>> '\x80'.decode('iso-8859-1', '
