import codecs
# Test codecs.register_error
def search(encoding):
    try:
        codec = codecs.lookup(encoding)
    except LookupError:
        print True
    else:
        print False
    return

search('no_such_encoding')
search('hex_codec')
