import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

# ##############  unicodedata.normalize() tests #####################

def ucd_norm(name, data):
    for src, norm in data:
        src = eval('"' + src + '"')
        norm = eval('"' + norm + '"')
        assert unicodedata.normalize(name, src) == norm, (
            "normalize(%s, %r) == %r != %r" %
            (name, src, unicodedata.normalize(name, src), norm))

NFD_DATA = [
    # ASCII source, NFD normalized.
    ("aaa", "aaa"),
    ("a\u030A", "\u00E5"),
    ("a\u030Aa", "a\u030AA"),
    ("a\u030Aa\u030A", "\u00E5A"),
    ("a\u030Aa\u030Aa", "a\u030AA\u030AA"),
    ("aaa\u030A", "a\u00
