import codecs
# Test codecs.register_error()

import codecs

def hex_decode(input, errors='strict'):
    return (input.replace(' ', '').decode('hex'), len(input))

def hex_encode(input, errors='strict'):
    return (input.encode('hex'), len(input))

codecs.register(hex_decode)
codecs.register(hex_encode)

print u'\u00e9'.encode('hex_codec')
print 'e9'.decode('hex_codec')

# Test codecs.lookup()

import codecs

def hex_decode(input, errors='strict'):
    return (input.replace(' ', '').decode('hex'), len(input))

def hex_encode(input, errors='strict'):
    return (input.encode('hex'), len(input))

codecs.register(hex_decode)
codecs.register(hex_encode)

print codecs.lookup('hex_codec').name
print
