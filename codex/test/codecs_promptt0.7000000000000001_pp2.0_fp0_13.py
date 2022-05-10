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

