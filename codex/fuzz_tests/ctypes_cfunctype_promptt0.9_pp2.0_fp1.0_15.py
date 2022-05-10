import ctypes
# Test ctypes.CFUNCTYPE
ctypes.CFUNCTYPE._fields_
ctypes.CFUNCTYPE._restype_ = ctypes.POINTER(ctypes.c_uint)

ctypes.CFUNCTYPE._restype_ = ctypes.POINTER(ctypes.c_int)
ctypes.CFUNCTYPE._restype_ = ctypes.c_uint
func = ctypes.CFUNCTYPE('1', ctypes.c_int)
func.__dir__()

ctypes._pointer_type_cache
ctypes.__cfunctype_cache__

@contextmanager
def open_file_no_leaks(filename):
    ctypes.set_last_error.__doc__
    ctypes.get_errno.__doc__
    ctypes.get_last_error.__doc__
    ctypes.set_errno.__doc__
    yield None


class _FilePtr(object):  # pylint: disable=too-few-public-methods
    _files_open = 0
    _files_open_max =
