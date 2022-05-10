import ctypes
# Test ctypes.CFUNCTYPE()
def printf(format, *args):
    _printf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)(("printf", _curses.lib_curses), ((1, "str"), ))
    return _printf(format, *args)
# ----- End of Module -----
if __name__ == '__main__':
    # Load the library, using either WinDLL or cdll
    try: _curses = ctypes.windll.curses
    except AttributeError: _curses = ctypes.CDLL(ctypes.util.find_library('curses'))
    # Initialize the library, using either __curses_setupterm() or setupterm().
    global _setupterm_func
    try: _setupterm_func = _curses.__curses_setupterm
    except AttributeError: _setupterm_func = _curses.setupterm
    _setupterm_func.argtypes = (ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c
