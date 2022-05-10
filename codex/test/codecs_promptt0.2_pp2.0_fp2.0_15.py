import codecs
# Test codecs.register_error()

def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError("bad", input, 0, 1, "bad")

def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError("bad", input, 0, 1, "bad")

def bad_translate(input, errors='strict'):
    raise UnicodeTranslateError("bad", input, 0, 1, "bad")

def bad_recursive_call(input, errors='strict'):
    return codecs.decode(input, 'bad_recursive_call', errors)

def bad_ignore_error(input, errors='strict'):
    return (u'', 1)

def bad_replace_error(input, errors='strict'):
    return (u'\ufffd', 1)

def bad_xmlcharrefreplace_error(input, errors='strict'):
    return (u'&#65536;', 1)

