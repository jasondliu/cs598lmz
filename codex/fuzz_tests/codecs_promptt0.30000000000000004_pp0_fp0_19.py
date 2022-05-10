import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('test.lookup', handler)

# Encode

encoder = codecs.getincrementalencoder('ascii')('test.lookup')
encoder.encode('\x80')
encoder.encode('\x80')
encoder.encode('\x80')

# Decode

decoder = codecs.getincrementaldecoder('ascii')('test.lookup')
decoder.decode('\x80')
decoder.decode('\x80')
decoder.decode('\x80')
