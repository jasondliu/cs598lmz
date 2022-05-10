import ctypes
# Test ctypes.CFUNCTYPE()
def printf(format, *args):
    _printf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(("printf", _curses.lib_curses), ((1, "str"), ))
    return _printf(format, *args)
# ----- End of Module -----
