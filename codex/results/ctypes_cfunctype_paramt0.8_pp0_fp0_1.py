import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p,
                           ctypes.c_int, ctypes.c_int, ctypes.c_int,
                           ctypes.c_int, ctypes.c_int, ctypes.c_int)



def printfunc(p_type, p_name, s_time, s_line, s_col, e_time, e_line,
              e_col):
    print("Type '%s', name '%s'" % (p_type, p_name))
    print("  start (%d, %d, %d)" % (s_time, s_line, s_col))
    print("  end   (%d, %d, %d)" % (e_time, e_line, e_col))



__all__ = ['getparser', 'print_cues']



def getparser(mimetype):
    """Returns a parser for the given mimetype or None if no parser is found.
    The returned parser implements the ``__call__`` method and takes a
