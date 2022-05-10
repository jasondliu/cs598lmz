import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(filename):
    """
    Get the encoding of a file.
    """
    file = open(filename, 'rb')
    try:
        rawdata = file.read(4096)
    finally:
        file.close()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    return charenc

def _get_encoding_from_file(file):
    """
    Get the encoding of a file.
    """
    try:
        rawdata = file.read(4096)
    finally:
        file.close()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    return charenc

def _get_encoding_from_string(string):
    """
    Get the encoding of a string.
    """
    result = chardet.detect(string)
    charenc = result['encoding']
    return charenc

def _
