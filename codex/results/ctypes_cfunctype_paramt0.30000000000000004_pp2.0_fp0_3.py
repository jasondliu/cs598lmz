import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def _make_function(name):
    return FUNTYPE(('_'+name).encode('ascii'))

_get_error = _make_function('get_error')
_get_error.restype = ctypes.c_char_p

_get_error_message = _make_function('get_error_message')
_get_error_message.restype = ctypes.c_char_p

_get_error_code = _make_function('get_error_code')
_get_error_code.restype = ctypes.c_int

_get_error_line = _make_function('get_error_line')
_get_error_line.restype = ctypes.c_int

_get_error_column = _make_function('get_error_column')
_get_error_column.restype = ctypes.c_int

_get_error_file = _make_function('get_error_file')
_get_error_file.restype = ctypes.c
