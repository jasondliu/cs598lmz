import codecs
# Test codecs.register_error
# Written by Marc-Andre Lemburg (mal@lemburg.com).
import codecs

def force_unicode(s):
    return s.decode('ascii')

def search_function(encoding):
    if encoding != 'test.register_error':
        return None
    return codecs.CodecInfo(
        name='test.register_error',
        encode=force_unicode,
        decode=force_unicode,
        incrementalencoder=None,
        incrementaldecoder=None,
        streamreader=None,
        streamwriter=None,
        )

