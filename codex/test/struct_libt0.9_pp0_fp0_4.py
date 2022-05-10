import _struct
import sys
from io import BytesIO

# ---------------------------

def _check_errno(result, _func, _arguments):
    if result >= 0:
        return result
    else:
        err = ctypes.get_errno()
        raise OSError(err, os.strerror(err))

# ---------------------------

# ---------- my stuff
_libnetbase = ctypes.CDLL('./_libnetbase.so', use_errno = True)


# ---------- my stuff

_libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno = True)


__iovec = _C_STRUCT_IOVEC
__iovec_p = __iovec * 1


# int sendfile(int out_fd, int in_fd, off_t *offset, size_t count);
# ssize_t sendfile(int out_fd, int in_fd, off_t offset, size_t count);
__sendfile = _libc.sendfile
__
