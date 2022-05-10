import codecs
# Test codecs.register_error

import codecs

class ExampleError(Exception):
    def __init__(self, reason):
        self.reason = reason
    def __str__(self):
        return repr(self.reason)

def search_function(encoding):
    if encoding != 'test.error':
        return None
    # This codec will raise an ExampleError exception when it
    # encounters bytes in the range 0x80-0xff
    utf8 = codecs.lookup('utf-8')
    return codecs.CodecInfo(
        name='test.error',
        encode=utf8.encode,
        decode=utf8.decode,
        incrementalencoder=utf8.incrementalencoder,
        incrementaldecoder=utf8.incrementaldecoder,
        streamreader=utf8.streamreader,
        streamwriter=utf8.streamwriter,
        _is_text_encoding=True,
    )

codecs.register(search_function)

# Now try the error handler

def error_handler(reason):
    raise ExampleError
