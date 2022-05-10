import codecs
codecs.register_error('strict', codecs.ignore_errors)


def open_utf8(filename, mode='r', encoding='utf-8'):
    """
    Open a file, with the given mode, in the given encoding.

    The default mode is 'r'. The default encoding is 'utf-8'.

    """
    return codecs.open(filename, mode, encoding)


def open_latin1(filename, mode='r', encoding='latin-1'):
    """
    Open a file, with the given mode, in the given encoding.

    The default mode is 'r'. The default encoding is 'latin-1'.

    """
    return codecs.open(filename, mode, encoding)


def open_strict(filename, mode='r', encoding='utf-8'):
    """
    Open a file, with the given mode, in the given encoding.

    The default mode is 'r'. The default encoding is 'utf-8'.

    """
    return codecs.open(filename, mode, encoding, 'strict')


def open_strict_latin1(filename
