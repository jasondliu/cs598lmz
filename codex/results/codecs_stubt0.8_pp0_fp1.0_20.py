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

escapes = [
# map of escape sequences to the associated single character,
# listed in order of frequency
# (source: http://www.w3.org/TR/html4/sgml/entities.html)
        (re.compile(r'&quot;'), '"'),
        (re.compile(r'&lt;'), '<'),
        (re.compile(r'&gt;'), '>'),
        (re.compile(r'&amp;'), '&'),
# A.2.2. Special characters
        (re.compile(r'&nbsp;'), '\u00A0'),
        (re.compile(r'&iexcl;'), '\u00A1'),
        (re.compile(r'&cent;'), '\u00A2'),
        (re.compile(r'&pound;'), '\u00A3'),
        (re.compile(r'&curren;'), '\u00A4'),
        (re.compile(r'&yen;'),
