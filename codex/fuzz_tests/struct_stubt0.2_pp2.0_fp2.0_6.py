from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# The following is a hack to get around the fact that the
# _struct module doesn't expose its internals.

import _struct

def _get_format_iter(fmt):
    """
    Return an iterator over the format string.
    """
    if isinstance(fmt, bytes):
        fmt = fmt.decode('ascii')
    return iter(fmt)

def _get_format_elem(fmt_iter):
    """
    Return the next format element.
    """
    fmt = next(fmt_iter)
    if fmt == 'x':
        return fmt, 1, 0
    if fmt in '@=<>!':
        return _get_format_elem(fmt_iter)
    if fmt in 'bBhHiIlLqQnN':
        return fmt, struct.calcsize(fmt), 0
    if fmt in 'fd':
        return fmt, struct.calcsize(fmt), 0
    if fmt == '
