import codecs
# Test codecs.register_error
# OK if it fails with a NotImplementedError on some platforms
def hexlify_call(c, errors='strict'):
    return codecs.charmap_encode(c, errors, encoding_map)[0]
testcodecs.register_error('test_error', hexlify_call)
testcodecs.register_error('test_ignore', hexlify_call)
testcodecs.register_error('test_replace', hexlify_call)
testcodecs.register_error('test_xmlcharrefreplace', hexlify_call)
testcodecs.register_error('test_backslashreplace', hexlify_call)
# Encode and decode communication
s = 'The quick brown fox jumped over the lazy dog.\n'
encoding_map = dict([(ord(c), c) for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
encoding_table = ''.join([chr(i) for i in xrange
