import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(path):
    """
    Return the encoding of the file at the given path.
    """
    with open(path, 'rb') as f:
        first_two_bytes = f.read(2)

    if first_two_bytes == codecs.BOM_UTF16_LE:
        return 'utf-16-le'
    elif first_two_bytes == codecs.BOM_UTF16_BE:
        return 'utf-16-be'
    elif first_two_bytes == codecs.BOM_UTF32_LE:
        return 'utf-32-le'
    elif first_two_bytes == codecs.BOM_UTF32_BE:
        return 'utf-32-be'
    elif first_two_bytes == codecs.BOM_UTF8:
        return 'utf-8-sig'
    else:
        return 'utf-8'

def _decode(text, encoding):
    """
    Return the decoded text.

