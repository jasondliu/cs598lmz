import _struct
# Test _struct.Struct

float_format = """
    # basic size and alignment tests for Float formats (L, l, f, d)
    >>> s = _struct.Struct('d')
    >>> s.size
    8
    >>> s.pack(0)
    '\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00'
    >>> import sys; sys.byteorder == "little" and "\\x00" or "\\x00"
    '\\x00'
    >>> import sys; sys.byteorder == "little" and "\\x00\\x00\\x00\\x00" or "\\x00\\x00\\x00\\x00"
    '\\x00\\x00\\x00\\x00'
    >>> import sys; sys.byteorder == "little" and "\\x00\\x00\\x00\\x00" or "\\x00\\x00\\x00\\x00"
    '\\x00\\x00\\x00\\x00'
    >>> import sys; sys.byteorder == "little" and "\\x
