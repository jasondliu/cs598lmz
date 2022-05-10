import codecs
# Test codecs.register_error()

import codecs

def handler(exc):
    print "HANDLER", exc
    return (u"", exc.end)

def search_function(encoding):
    if encoding != 'test.unicode':
        return None
    return codecs.CodecInfo(
        name='test.unicode',
        encode=None,
        decode=None,
        incrementalencoder=None,
        incrementaldecoder=None,
        streamreader=None,
        streamwriter=None,
        _is_text_encoding=True)

codecs.register(search_function)

unicode('a').encode('test.unicode', 'test.unicode')

codecs.register_error('test.unicode', handler)

unicode('a').encode('test.unicode', 'test.unicode')

codecs.register_error('test.unicode', None)

unicode('a').encode('test.unicode', 'test.unicode')

codecs.register_error('test.unicode
