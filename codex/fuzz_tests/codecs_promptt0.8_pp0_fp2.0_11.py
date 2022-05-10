import codecs
# Test codecs.register_error for embedded 'strict' error handler

handler_map = codecs.make_identity_dict(range(256))
handler_map[ord(u'\u3042')] = codecs.strict_error

def search_function(encoding):
    if encoding != 'test.unicode_escape2':
        return None
    utf8 = codecs.lookup('utf-8')
    return codecs.CodecInfo(
        name='test.unicode_escape2',
        encode=utf8.encode,
        decode=utf8.decode,
        incrementalencoder=utf8.incrementalencoder,
        incrementaldecoder=utf8.incrementaldecoder,
        streamreader=utf8.streamreader,
        streamwriter=utf8.streamwriter,
        encodeerror=handler_map.get,
        decodeerror=handler_map.get)

codecs.register(search_function)

def test(error_handler=handler_map.get):
    s = '\\u3042'
    u = u'\
