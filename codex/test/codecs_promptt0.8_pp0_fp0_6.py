import codecs
# Test codecs.register_error
codecs.register_error('myerror', codecs.replace_errors)
def py_encode(t):
    return t.encode('hex')
def py_decode(t):
    return t.decode('hex')
