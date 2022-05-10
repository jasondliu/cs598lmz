import codecs
codecs.register_error('my_replace', codecs.lookup_error('replace'))

def _unicode_to_str(unicode_str):
    """
    Converts a unicode string to a string in the current encoding.
    """
    return unicode_str.encode(sys.getdefaultencoding(), 'my_replace')

def _str_to_unicode(str):
    """
    Converts a string to a unicode string.
    """
    return str.decode(sys.getdefaultencoding(), 'my_replace')

def _get_encoding(filename):
    """
    Returns the encoding of the file given by filename.
    """
    file_descriptor = open(filename, 'r')
    try:
        encoding = file_descriptor.encoding
    finally:
        file_descriptor.close()
    return encoding

def _get_encoding_from_file(file):
    """
    Returns the encoding of the given file.
    """
    return file.encoding

def _unicode_to_str_in
