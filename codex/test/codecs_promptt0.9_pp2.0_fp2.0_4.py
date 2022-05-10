import codecs
# Test codecs.register_error
def ucs2_to_utf8_errorhandler(error):
    return (u'\uFFFD', error.end)
codecs.register_error('unicode-ucs2-replace', ucs2_to_utf8_errorhandler)
codecs.register_error('unicode-ucs2-skip', lambda e: ('', e.end))
# Test hexadecimal, octal, and binary literals
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0, 0, 0, 0, 0o0000, 0o0000, 0b0000, 0b000
# Test percent sign literal
