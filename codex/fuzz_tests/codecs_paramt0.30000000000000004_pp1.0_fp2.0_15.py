import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(text):
    """
    Return the encoding of the given text.
    """
    if isinstance(text, unicode):
        return 'utf-8'
    else:
        return 'latin1'

def _encode(text, encoding):
    """
    Encode the given text with the given encoding.
    """
    if isinstance(text, unicode):
        return text.encode(encoding)
    else:
        return text

def _decode(text, encoding):
    """
    Decode the given text with the given encoding.
    """
    if isinstance(text, unicode):
        return text
    else:
        return text.decode(encoding, 'strict')

def _get_encoded_lines(text):
    """
    Return the given text as a list of encoded lines.
    """
    encoding = _get_encoding(text)
    if isinstance(text, unicode):
        return text.splitlines()
   
