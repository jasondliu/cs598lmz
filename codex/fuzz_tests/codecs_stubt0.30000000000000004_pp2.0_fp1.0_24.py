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

# The following tests are copied from test_unicode.py

# test decoding with errors
def test_decoding_errors(encoding):
    if encoding in ('iso2022_jp', 'iso2022_jp_2', 'iso2022_kr',
                    'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext',
                    'shift_jis_2004', 'hz'):
        # iso2022 codecs don't support error handling
        return
    if encoding in ('utf_7', 'utf_8_sig'):
        # utf_7 and utf_8_sig codecs don't support surrogates
        return
    if encoding in ('idna', 'punycode', 'unicode_internal'):
        # idna, punycode and unicode_internal codecs don't support
        # surrogates
        return
    if encoding in ('raw_unicode_escape', 'raw_unicode_escape_8bit'):
        # raw_unicode_escape and raw_unicode_escape_
