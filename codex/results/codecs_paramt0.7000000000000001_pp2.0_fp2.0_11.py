import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

def utf8_encode(string):
    """
    Return an utf-8 encoded string
    """
    return string.encode('utf-8')

def utf8_decode(string):
    """
    Return the string from utf-8 encoding
    """
    return string.decode('utf-8')

def latin_encode(string):
    """
    Return an iso-8859-1 encoded string
    """
    return string.encode('iso-8859-1')

def latin_decode(string):
    """
    Return the string from iso-8859-1 encoding
    """
    return string.decode('iso-8859-1', 'strict')

def utf8_to_latin(string, strict=True):
    """
    Return the string from utf-8 encoding to iso-8859-1 encoding
    """
    if strict:
        return utf8_decode(string).encode('iso-8859
