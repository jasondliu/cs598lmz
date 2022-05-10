import codecs
# Test codecs.register_error()

import codecs

def replace_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'\ufffd', exc.end)
    else:
        # call default handler for encoding errors
        return codecs.strict_errors(exc)

def search_function(encoding):
    if encoding != 'test.replace_error':
        return None
    else:
        return codecs.CodecInfo(
            name='test.replace_error',
            encode=codecs.strict_encode,
            decode=codecs.strict_decode,
            incrementalencoder=None,
            incrementaldecoder=None,
            streamwriter=None,
            streamreader=None,
            _is_text_encoding=True,
            )

codecs.register(search_function)
codecs.register_error('test.replace_error', replace_error)

encoding = 'test.replace_error'

# encode
print 'encoding:', encoding
for s in [u'\
