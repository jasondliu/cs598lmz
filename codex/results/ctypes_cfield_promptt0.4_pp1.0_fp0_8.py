import ctypes
# Test ctypes.CField

if __name__ == '__main__':
    import sys
    import os
    import unittest
    from test import support

    support.requires('ctypes')

    # ctypes.CField is used by the parser
    # to store the offset and the type of a field
    # in a ctypes Structure or Union.
    # It's also used to store the offset of the
    # function address in a function pointer.
    #
    # XXX It's not used for bitfields yet
    #
    # It's a subclass of int, and provides a
    # _type_ attribute.
    #
    # The _type_ attribute is used to convert
    # the integer value to the appropriate ctypes
    # type.  For example, in a Structure, it's
    # used to convert the integer value to a c_char,
    # c_short, c_int, c_long, c_longlong, c_float,
    # c_double, c_void_p, or a c_char_p.
    #
    # In a function pointer, it's used to
