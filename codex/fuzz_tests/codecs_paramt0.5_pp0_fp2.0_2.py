import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(file):
    """Get the encoding of a file.

    :param file: The file to get the encoding for.
    :returns: The encoding of the file.
    :rtype: str

    """
    f = open(file, 'r')
    try:
        return chardet.detect(f.read())['encoding']
    finally:
        f.close()

def _get_encoding_errors(file, encoding):
    """Get the errors of a file.

    :param file: The file to get the errors for.
    :param encoding: The encoding of the file.
    :returns: The errors of the file.
    :rtype: str

    """
    f = open(file, 'r')
    try:
        return f.read().decode(encoding, 'strict')
    finally:
        f.close()

def _get_encoding_errors_list(file, encoding):
    """Get the errors of a file.

    :
