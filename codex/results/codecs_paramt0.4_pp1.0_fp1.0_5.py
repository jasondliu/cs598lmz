import codecs
codecs.register_error('strict', codecs.ignore_errors)

# ----------------------------------------------------------------------
# Constants

# ----------------------------------------------------------------------
# Globals

# ----------------------------------------------------------------------
# Functions for external use

def decode(data, encoding="utf-8"):
    """
    Decode a string from a given encoding, or utf-8 if not specified.
    """
    if isinstance(data, bytes):
        return data.decode(encoding, 'strict')
    else:
        return data

def encode(data, encoding="utf-8"):
    """
    Encode a string to a given encoding, or utf-8 if not specified.
    """
    if isinstance(data, bytes):
        return data
    else:
        return data.encode(encoding, 'strict')

def decode_if_bytes(data, encoding="utf-8"):
    """
    Decode a string from a given encoding, or utf-8 if not specified,
    if it is a bytes object.
    """
    if isinstance(data, bytes):
        return data.decode
