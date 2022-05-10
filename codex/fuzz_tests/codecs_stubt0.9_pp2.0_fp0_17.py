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

class DecodeTestSequence:
    # test sequences for the decoder
    testseqs = [
        ('a', "add_one_codepoint"),
        ('a\u0100', "add_one_codepoint"),
        ('a\u3042', "add_one_codepoint"),
        ('a\U00010F69', "add_one_codepoint"),
        ('a\uD800', "add_one_codepoint"),
        ('a\uD800\uDC00', "add_one_codepoint"),
        ('a\ud834\udd1e', "add_one_codepoint"),
        ('a\U0010FFFF', "add_one_codepoint"),

        ('a', "add_utf16_byteseq"),
        ('b', "add_utf32_byteseq"),
        ('c', "add_encoding_name"),
        ('d', "add_utf16_bytes"),
        ('e', "add_utf32_bytes"),
    ]

    # error handling flags used
