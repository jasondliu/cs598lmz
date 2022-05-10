import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('my_error', my_error_handler)

# This codec is broken, but we can still use it with the error handler
codecs.register(lambda name: codecs.lookup('ascii') if name == 'my_codec' else None)

for encoding in ['my_codec', 'my_codec_error']:
    print('Encoding:', encoding)
