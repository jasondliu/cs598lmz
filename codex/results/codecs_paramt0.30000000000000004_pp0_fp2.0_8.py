import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import _py2to3

def _get_encoding(filename):
    """
    Get the encoding of a file.

    :param filename: The name of the file.
    :return: The encoding of the file.
    """
    with open(filename, 'rb') as f:
        raw = f.read(4)
    if raw.startswith(codecs.BOM_UTF32_LE):
        return 'utf-32-le'
    elif raw.startswith(codecs.BOM_UTF32_BE):
        return 'utf-32-be'
    elif raw.startswith(codecs.BOM_UTF16_LE):
        return 'utf-16-le'
    elif raw.startswith(codecs.BOM_UTF16_BE):
        return 'utf-16-be'
    elif raw.startswith(codecs.BOM_UTF8):
        return 'utf-8-sig'
    else:

