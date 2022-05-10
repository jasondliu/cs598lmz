import codecs
# Test codecs.register_error

def test(encoding):
    try:
        codecs.lookup(encoding)
    except LookupError:
        try:
            import encodings
            encodings._cache.clear()
            encodings._unknown.clear()
            encodings._aliases.clear()
        except ImportError:
            pass
        raise
    text = u"abc\u3042\u3044\u3046\u3048\u304a"
    encoder = codecs.getencoder(encoding)
    decoder = codecs.getdecoder(encoding)
