import codecs
# Test codecs.register_error
# OK if it fails with a NotImplementedError on some platforms
def hexlify_call(c, errors='strict'):
    return codecs.charmap_encode(c, errors, encoding_map)[0]
