import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Python 2/3 compatibility
from six import PY3

def decode_path(path):
    """
    Decode a path to the filesystem encoding with 'surrogateescape' error
    handler, so undecodable bytestrings still result in a string object (instead
    of raising an exception).
    """
    if PY3:
        return path
    else:
        return path.decode(sys.getfilesystemencoding(), 'surrogateescape')

def encode_path(path):
    """
    Encode a path to the filesystem encoding with 'surrogateescape' error
    handler, so undecodable bytestrings still result in a string object (instead
    of raising an exception).
    """
    if PY3:
        return path
    else:
        return path.encode(sys.getfilesystemencoding(), 'surrogateescape')

def decode_filename(filename):
    """
    Decode a filename to the filesystem encoding with 'strict' error handler,
    so undecod
