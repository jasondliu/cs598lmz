import gc, weakref, functools
from . import _cffi_backend
from ._cffi_backend import (FFI, FFIError, CType, CTypeEnum, CTypeArray,
                            CTypedef, CDataOwning, CData,
                            sizeof, alignof, addressof, typeof, new,
                            callback, getcname, cast, string,
                            unpack, pack, memmove, memset,
                            library, dlopen, dlclose, dlsym, get_errno,
                            set_errno,
                            CDLL, PYFUNCTYPE, RTLD_LOCAL, RTLD_GLOBAL,
                            RTLD_NOW, RTLD_DEFAULT, RTLD_NEXT, RTLD_NODELETE,
                            RTLD_LAZY, RTLD_NOLOAD)
from ._cffi_backend import *     # for __doc__
from ._cffi_backend import _cffi_opcode_intern_python, _make_ffi_library


_
