import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding != 'test.searchfunction':
        return None
    codecs.register_error('test.searchfunction', codecs.replace_errors)
    return codecs.CodecInfo(
        name='test.searchfunction',
        encode=codecs.charmap_encode,
        decode=codecs.charmap_decode,
        incrementalencoder=codecs.IncrementalEncoder,
        incrementaldecoder=codecs.IncrementalDecoder,
        streamreader=codecs.StreamReader,
        streamwriter=codecs.StreamWriter,
    )


codecs.register(search_function)

# Test codecs.lookup_error()

def replace_errors(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return (u'\ufffd', exc.end)

