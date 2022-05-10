import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object,
                           ctypes.c_int, ctypes.py_object)


def libparse_default_tab_width():
    """
    Return the libparse default tab width.

    Return the libparse default tab width. This may be an integer, or None if
    there is no default tab width.
    """

    return libparse_wrapper.parse_default_tab_width()


def libparse_line_width():
    """
    Return the libparse line width.

    Return the libparse line width. This is the number of characters in each
    line. This may be an integer, or None if there is no line width.
    """

    return libparse_wrapper.parse_line_width()


def libparse_set_default_tab_width(width):
    """
    Set the libparse default tab width.

    Set the libparse default tab width for parsing. Pass in an integer, or
    None to cause the default tab width to be unset.
    """

    libparse_wrapper.parse_set_default_tab_width(width)


